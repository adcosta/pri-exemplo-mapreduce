# Descarrega uma imagem Ubuntu 20
FROM ubuntu:20.04

# Define o maintainer
LABEL maintainer="Nome Apelido <email@exemplo.com>"

# Define variáveis de ambiente para evitar perguntas durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala dependências básicas
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk wget curl python3 python3-pip vim nano git ssh \
    && rm -rf /var/lib/apt/lists/*

# Define JAVA_HOME (calculado dinamicamente para funcionar em amd64 e arm64)
RUN JAVA_PATH=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "export JAVA_HOME=$JAVA_PATH" >> /root/.bashrc && \
    echo "export PATH=$JAVA_PATH/bin:$PATH" >> /root/.bashrc

# Versão do Hadoop — pode ser substituída em tempo de build:
#   docker build --build-arg HADOOP_VERSION=3.4.4 -t mapreduce-ir .
ARG HADOOP_VERSION=3.4.3
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xvzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} /usr/local/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Configure Hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
RUN echo "export HADOOP_HOME=$HADOOP_HOME" >> /root/.bashrc && \
    echo "export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH" >> /root/.bashrc

# Regista JAVA_HOME em hadoop-env.sh para que o Hadoop o encontre sempre,
# mesmo em sessões não-interactivas (onde .bashrc não é carregado)
RUN JAVA_PATH=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "export JAVA_HOME=$JAVA_PATH" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Cria uma pasta de trabalho e define como diretório padrão
WORKDIR /workspace
COPY colecao.txt /workspace/
COPY mapper.py /workspace/
COPY reducer.py /workspace/
COPY comando.hadoop /workspace/

RUN java -version # && hadoop version && spark-submit --version

# Comando padrão ao iniciar o container (shell interativo)
CMD ["/bin/bash"]
