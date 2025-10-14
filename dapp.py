# dapp.py

from os import environ
import logging
import requests
import json
import joblib
import pandas as pd
import numpy as np
import traceback

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

# --- 1. CARREGANDO OS ARTEFATOS DO MODELO NA INICIALIZAÇÃO ---
try:
    model = joblib.load('decision_tree_model.joblib')
    with open('model_columns.json', 'r') as f:
        model_columns = json.load(f)
    with open('target_map.json', 'r') as f:
        target_map = {int(k): v for k, v in json.load(f).items()}
    logger.info("Modelo de ML e artefatos carregados com sucesso!")
except Exception as e:
    logger.error(f"ERRO CRÍTICO: Não foi possível carregar os artefatos do modelo: {e}")
    model, model_columns, target_map = None, None, None

# --- 2. FUNÇÕES AUXILIARES DE CONVERSÃO ---
def hex2str(hex_string):
    return bytes.fromhex(hex_string[2:]).decode("utf-8")

def str2hex(string):
    return "0x" + string.encode("utf-8").hex()

# --- 3. LÓGICA PRINCIPAL QUE RECEBE INPUTS DA BLOCKCHAIN ---
def handle_advance(data):
    logger.info(f"Recebida requisição de avanço (input da blockchain)")

    if not all([model, model_columns, target_map]):
        error_msg = "Modelo de ML não está carregado. Rejeitando input."
        logger.error(error_msg)
        # Envia um "report" que pode ser lido para depuração
        requests.post(rollup_server + "/report", json={"payload": str2hex(error_msg)})
        return "reject"

    try:
        # Decodifica o payload da transação (esperamos um JSON)
        payload_str = hex2str(data['payload'])
        input_data = json.loads(payload_str)
        logger.info(f"Payload (dados do paciente) recebido: {input_data}")
        
        # Prepara o DataFrame para o modelo (lógica idêntica à da API)
        input_df = pd.DataFrame(columns=model_columns, index=[0]).fillna(0)
        
        for feature, value in input_data.items():
            if feature in input_df.columns:
                input_df.loc[0, feature] = value
        
        input_df = input_df[model_columns] # Garante a ordem correta

        # Faz a predição
        prediction_encoded = model.predict(input_df)
        diagnosis = target_map.get(prediction_encoded[0], "Classe desconhecida")
        logger.info(f"Diagnóstico do modelo: {diagnosis}")

        # Cria um JSON de resultado e o envia como uma "notice" para a blockchain
        result_json = json.dumps({"diagnostico_provavel": diagnosis, "input_recebido": input_data})
        notice = {"payload": str2hex(result_json)}
        response = requests.post(rollup_server + "/notice", json=notice)
        logger.info(f"Notice enviada com o diagnóstico, status {response.status_code}")
        
        return "accept"

    except Exception as e:
        error_msg = f"Erro ao processar o input: {traceback.format_exc()}"
        logger.error(error_msg)
        requests.post(rollup_server + "/report", json={"payload": str2hex(error_msg)})
        return "reject"

def handle_inspect(data):
    logger.info(f"Recebida requisição de inspeção (leitura off-chain)")
    payload_str = hex2str(data['payload'])
    logger.info(f"Payload de inspeção: {payload_str}")
    report = {"payload": str2hex(f"O DApp está online. Envie um 'advance' com o JSON dos dados do paciente.")}
    requests.post(rollup_server + "/report", json=report)
    return "accept"

# --- CÓDIGO BOILERPLATE DA CARTESI ---
handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

while True:
    logger.info("Aguardando próximo input da blockchain...")
    response = requests.post(rollup_server + "/finish", json=finish)
    if response.status_code == 202:
        logger.info("Nenhum input pendente.")
    else:
        rollup_request = response.json()
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])