# PySpark + JupyterLab para o exercício de IR
# Construir a partir da pasta pai:
#   docker build -f spark/Dockerfile -t ir-spark .

FROM python:3.11-slim

# Java é obrigatório — o Spark corre na JVM mesmo quando usado via Python
# Usa default-jdk para ser compatível com qualquer versão de Debian/Ubuntu e arm64/amd64
RUN apt-get update && apt-get install -y \
    default-jdk procps \
    && rm -rf /var/lib/apt/lists/*

# Instala PySpark e JupyterLab
RUN pip install --no-cache-dir pyspark jupyterlab

# Cria pasta de trabalho e copia ficheiros do exercício
WORKDIR /workspace
COPY colecao.txt        /workspace/
COPY colecao_grande.txt /workspace/
COPY spark/ir_spark_1_indice.ipynb /workspace/
COPY spark/ir_spark_2_tfidf.ipynb  /workspace/

# Script de arranque (define JAVA_HOME e lança Jupyter)
COPY spark/start-jupyter.sh /start-jupyter.sh
RUN chmod +x /start-jupyter.sh

# Spark UI (4040) e JupyterLab (8888)
EXPOSE 8888 4040

CMD ["/start-jupyter.sh"]
