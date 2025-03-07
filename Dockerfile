# Descareega  uma imagem Ubuntu 20
FROM ubuntu:20.04

# Define o maintainer
LABEL maintainer="Nome Apelido <email@exemplo.com>"

# Define variáveis de ambiente para evitar perguntas durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala dependências básicas
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk wget curl python3 python3-pip vim nano git ssh \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME for Hadoop and Spark
RUN export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "export JAVA_HOME=$JAVA_HOME" >> /etc/profile &&\
    echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile && \ 
    echo "export JAVA_HOME=$JAVA_HOME" >> /root/.bashrc &&\
    echo "export PATH=$JAVA_HOME/bin:$PATH" >> /root/.bashrc 

# Install Hadoop 3.4.1
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz && \
    tar -xvzf hadoop-3.4.1.tar.gz && \
    mv hadoop-3.4.1 /usr/local/hadoop && \
    rm hadoop-3.4.1.tar.gz

# Configure Hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
RUN export HADOOP_HOME=/usr/local/hadoop && \
    echo "export HADOOP_HOME=$HADOOP_HOME" >> /root/.bashrc &&\
    echo "export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH" >> /root/.bashrc 

# Baixa e instala o Spark
RUN wget https://downloads.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz && \
    tar -xvzf spark-3.5.5-bin-hadoop3.tgz && \
    mv spark-3.5.5-bin-hadoop3 /usr/local/spark && \
    rm spark-3.5.5-bin-hadoop3.tgz

# Configura variáveis de ambiente para o Spark
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$SPARK_HOME/bin:$PATH
RUN export SPARK_HOME=/usr/local/spark && \
    echo "export SPARK_HOME=$SPARK_HOME" >> /root/.bashrc &&\
    echo "export PATH=$HSPARK_HOME/bin:$PATH" >> /root/.bashrc 


# Instala dependências do Python para Spark
RUN pip3 install pyspark

# Cria uma pasta de trabalho e define como diretório padrão
WORKDIR /workspace
COPY colecao.txt /workspace/
COPY mapper.py /workspace/
COPY reducer.py /workspace/
COPY comando.hadoop /workspace/

RUN java -version # && hadoop version && spark-submit --version

# Comando padrão ao iniciar o container (shell interativo)
CMD ["/bin/bash"]
