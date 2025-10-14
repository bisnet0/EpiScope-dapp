# syntax=docker.io/docker/dockerfile:1

# --- ESTÁGIO 1: O CONSTRUTOR DE "WHEELS" ---
# Este estágio é responsável pela parte lenta: compilar as dependências.
# O resultado dele será um diretório com pacotes .whl pré-compilados para RISC-V.
FROM --platform=linux/riscv64 cartesi/python:3.10-slim-jammy AS builder

# 1. Instala as ferramentas de compilação necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Copia o arquivo de dependências
COPY ./requirements.txt .

# 3. O "Pulo do Gato": Compila todas as dependências e as transforma em "wheels"
# Este comando cria um pacote .whl para cada dependência e o salva em /wheels
# Esta é a etapa que demora, mas que será cacheada pelo Docker
RUN pip wheel --wheel-dir=/wheels -r requirements.txt


# --- ESTÁGIO 2: A IMAGEM FINAL DO DAPP ---
# Este estágio é rápido e limpo. Ele não precisa de ferramentas de compilação.
FROM --platform=linux/riscv64 cartesi/python:3.10-slim-jammy

# Instala as ferramentas da Cartesi (mesmo de antes)
ARG MACHINE_EMULATOR_TOOLS_VERSION=0.14.1
ADD https://github.com/cartesi/machine-emulator-tools/releases/download/v${MACHINE_EMULATOR_TOOLS_VERSION}/machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb /
RUN dpkg -i /machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb \
  && rm /machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb

# Instala o busybox e cria o usuário (mesmo de antes)
RUN apt-get update && \
    apt-get install -y --no-install-recommends busybox-static=1:1.30.1-7ubuntu3 && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --create-home --user-group dapp

ENV PATH="/opt/cartesi/bin:${PATH}"
WORKDIR /opt/cartesi/dapp

# 1. Copia os "wheels" pré-compilados do Estágio 1
COPY --from=builder /wheels /wheels

# 2. Instala as dependências a partir dos "wheels" locais.
# Esta etapa agora é MUITO RÁPIDA, pois não há compilação.
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* && \
    rm -rf /wheels # Limpa os arquivos de instalação

# 3. Copia o resto da sua aplicação (artefatos de ML e o dapp.py)
COPY decision_tree_model.joblib .
COPY model_columns.json .
COPY target_map.json .
COPY ./dapp.py .

ENV ROLLUP_HTTP_SERVER_URL="http://127.0.0.1:5004"

ENTRYPOINT ["rollup-init"]
CMD ["python3", "dapp.py"]