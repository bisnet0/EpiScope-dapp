# dapp.py (versão final, otimizada e leve)

from os import environ
import logging
import requests
import json
import traceback

# 🗑️ REMOVEMOS os imports do pandas, numpy e joblib!

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")


# ✨ NOVA FUNÇÃO DE PREDIÇÃO ✨
def predict_diagnosis(input_data):
# --- INÍCIO DAS REGRAS ---
    if input_data.get('febre', 0) <= 0.5000:
        if input_data.get('ns1_encoded', 0) <= -50.5000:
            if input_data.get('criterio_0', 0) <= 0.5000:
                if input_data.get('cefaleia', 0) <= 0.5000:
                    if input_data.get('criterio_2', 0) <= 0.5000:
                        if input_data.get('idade', 0) <= 4037.5000:
                            if input_data.get('sexo_encoded', 0) <= 0.5000:
                                if input_data.get('idade', 0) <= 3506.0000:
                                    if input_data.get('idade', 0) <= 2003.0000:
                                        if input_data.get('idade', 0) <= 2000.5000:
                                            return 'zika'
                                        else:
                                            return 'dengue'
                                    else:
                                        return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4036.5000:
                                        if input_data.get('idade', 0) <= 4028.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        return 'zika'
                            else:
                                if input_data.get('idade', 0) <= 4013.5000:
                                    if input_data.get('idade', 0) <= 2503.0000:
                                        return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4011.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                                else:
                                    if input_data.get('idade', 0) <= 4028.5000:
                                        if input_data.get('idade', 0) <= 4026.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4030.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'zika'
                        else:
                            if input_data.get('mialgia', 0) <= 0.5000:
                                if input_data.get('nausea', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4061.5000:
                                        if input_data.get('idade', 0) <= 4059.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('petequia_n', 0) <= 0.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'dengue'
                                else:
                                    if input_data.get('idade', 0) <= 4039.5000:
                                        return 'dengue'
                                    else:
                                        return 'dengue'
                            else:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    return 'dengue'
                                else:
                                    return 'dengue'
                    else:
                        if input_data.get('idade', 0) <= 4062.5000:
                            if input_data.get('sexo_encoded', 0) <= 0.5000:
                                if input_data.get('idade', 0) <= 4061.5000:
                                    if input_data.get('idade', 0) <= 4041.5000:
                                        if input_data.get('idade', 0) <= 4022.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4056.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                                else:
                                    return 'zika'
                            else:
                                if input_data.get('idade', 0) <= 4037.5000:
                                    if input_data.get('idade', 0) <= 2019.5000:
                                        if input_data.get('idade', 0) <= 2000.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('idade', 0) <= 4001.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                else:
                                    if input_data.get('idade', 0) <= 4039.5000:
                                        if input_data.get('idade', 0) <= 4038.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4059.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                        else:
                            if input_data.get('idade', 0) <= 4085.5000:
                                if input_data.get('idade', 0) <= 4073.5000:
                                    if input_data.get('idade', 0) <= 4071.5000:
                                        if input_data.get('artrite', 0) <= 0.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'dengue'
                                    else:
                                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4075.5000:
                                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('idade', 0) <= 4083.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                            else:
                                return 'zika'
                else:
                    if input_data.get('nausea', 0) <= 0.5000:
                        return 'dengue'
                    else:
                        return 'dengue'
            else:
                if input_data.get('idade', 0) <= 4029.5000:
                    if input_data.get('cefaleia', 0) <= 0.5000:
                        if input_data.get('idade', 0) <= 4013.5000:
                            if input_data.get('idade', 0) <= 2022.5000:
                                if input_data.get('idade', 0) <= 2000.5000:
                                    return 'zika'
                                else:
                                    return 'dengue'
                            else:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4001.5000:
                                        if input_data.get('idade', 0) <= 3506.0000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('sexo_encoded', 0) <= -0.5000:
                                            return 'dengue'
                                        else:
                                            return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4003.5000:
                                        if input_data.get('idade', 0) <= 3005.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4004.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'zika'
                        else:
                            if input_data.get('idade', 0) <= 4019.5000:
                                if input_data.get('idade', 0) <= 4018.5000:
                                    if input_data.get('idade', 0) <= 4017.5000:
                                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                else:
                                    if input_data.get('sexo_encoded', 0) <= 0.5000:
                                        return 'zika'
                                    else:
                                        return 'zika'
                            else:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4020.5000:
                                        return 'dengue'
                                    else:
                                        if input_data.get('idade', 0) <= 4028.5000:
                                            return 'zika'
                                        else:
                                            return 'dengue'
                                else:
                                    if input_data.get('idade', 0) <= 4024.5000:
                                        if input_data.get('idade', 0) <= 4023.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('idade', 0) <= 4025.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                    else:
                        return 'dengue'
                else:
                    if input_data.get('idade', 0) <= 4030.5000:
                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                            return 'chikungunya'
                        else:
                            return 'chikungunya'
                    else:
                        if input_data.get('idade', 0) <= 4047.5000:
                            if input_data.get('idade', 0) <= 4045.5000:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4039.5000:
                                        if input_data.get('idade', 0) <= 4037.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('idade', 0) <= 4044.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                else:
                                    if input_data.get('idade', 0) <= 4034.5000:
                                        if input_data.get('idade', 0) <= 4032.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4035.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'zika'
                            else:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4046.5000:
                                        return 'zika'
                                    else:
                                        return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4046.5000:
                                        return 'zika'
                                    else:
                                        return 'zika'
                        else:
                            if input_data.get('idade', 0) <= 4075.5000:
                                if input_data.get('idade', 0) <= 4064.5000:
                                    if input_data.get('idade', 0) <= 4061.5000:
                                        if input_data.get('idade', 0) <= 4060.5000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('sexo_encoded', 0) <= 0.5000:
                                            return 'zika'
                                        else:
                                            return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4068.5000:
                                        if input_data.get('idade', 0) <= 4067.5000:
                                            return 'chikungunya'
                                        else:
                                            return 'chikungunya'
                                    else:
                                        if input_data.get('idade', 0) <= 4074.0000:
                                            return 'zika'
                                        else:
                                            return 'chikungunya'
                            else:
                                if input_data.get('sexo_encoded', 0) <= 0.5000:
                                    if input_data.get('idade', 0) <= 4084.0000:
                                        if input_data.get('idade', 0) <= 4081.0000:
                                            return 'dengue'
                                        else:
                                            return 'dengue'
                                    else:
                                        return 'zika'
                                else:
                                    if input_data.get('idade', 0) <= 4079.5000:
                                        return 'zika'
                                    else:
                                        if input_data.get('idade', 0) <= 4083.0000:
                                            return 'zika'
                                        else:
                                            return 'zika'
        else:
            if input_data.get('petequia_n', 0) <= 0.5000:
                return 'dengue'
            else:
                return 'dengue'
    else:
        if input_data.get('criterio_1', 0) <= 0.5000:
            return 'dengue'
        else:
            return 'dengue'

# --- FIM DAS REGRAS ---


# --- Funções Auxiliares (sem alteração) ---
def hex2str(hex_string):
    return bytes.fromhex(hex_string[2:]).decode("utf-8")

def str2hex(string):
    return "0x" + string.encode("utf-8").hex()


# --- Lógica Principal (simplificada) ---
def handle_advance(data):
    logger.info(f"Recebida requisição de avanço (input da blockchain)")

    try:
        # Decodifica o payload da transação para um dicionário Python
        payload_str = hex2str(data['payload'])
        input_data = json.loads(payload_str)
        logger.info(f"Payload (dados do paciente) recebido: {input_data}")
        
        # ⚙️ CHAMA A NOVA FUNÇÃO DE PREDIÇÃO ⚙️
        diagnosis = predict_diagnosis(input_data)
        logger.info(f"Diagnóstico do modelo: {diagnosis}")

        # Cria um JSON de resultado e o envia como uma "notice"
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
    # Esta função não muda
    logger.info(f"Recebida requisição de inspeção")
    report = {"payload": str2hex("O DApp de diagnóstico está online.")}
    requests.post(rollup_server + "/report", json=report)
    return "accept"


# --- Código Boilerplate da Cartesi (sem alteração) ---
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