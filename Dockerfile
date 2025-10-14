# Dockerfile (Versão Final, Leve e Funcional)

# 1. Imagem base padrão da Cartesi
FROM --platform=linux/riscv64 cartesi/python:3.10-slim-jammy

# 2. Instala as ferramentas essenciais da Cartesi (a "chave de ignição")
ARG MACHINE_EMULATOR_TOOLS_VERSION=0.14.1
ADD https://github.com/cartesi/machine-emulator-tools/releases/download/v${MACHINE_EMULATOR_TOOLS_VERSION}/machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb /
RUN dpkg -i /machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb \
  && rm /machine-emulator-tools-v${MACHINE_EMULATOR_TOOLS_VERSION}.deb

# 3. Instala o busybox e cria o usuário (padrão de segurança da Cartesi)
RUN apt-get update && \
    apt-get install -y --no-install-recommends busybox-static=1:1.30.1-7ubuntu3 && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --create-home --user-group dapp

# 4. Define o diretório de trabalho
WORKDIR /opt/cartesi/dapp

# 5. Instala as dependências leves do seu DApp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o script principal do DApp
COPY dapp.py .

# 7. Define o ENTRYPOINT e CMD corretos para a Cartesi
# O `rollup-init` é o programa principal que o Cartesi OS executa.
# Ele, por sua vez, vai chamar o seu `python3 dapp.py`.
ENV ROLLUP_HTTP_SERVER_URL="http://127.0.0.1:5004"
ENTRYPOINT ["rollup-init"]
CMD ["python3", "dapp.py"]