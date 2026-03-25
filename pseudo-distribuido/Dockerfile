# Hadoop em modo pseudo-distribuído
# Construir a partir da pasta pai:
#   docker build -f pseudo-distribuido/Dockerfile -t mapreduce-pseudo .

FROM ubuntu:20.04

LABEL maintainer="Nome Apelido <email@exemplo.com>"

ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências — SSH e sudo são obrigatórios para o Hadoop arrancar os daemons
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk wget curl python3 python3-pip vim nano git ssh sudo \
    && rm -rf /var/lib/apt/lists/*

# Configura SSH sem password para localhost (exigido pelo Hadoop pseudo-distribuído)
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys
RUN printf "Host localhost\n    StrictHostKeyChecking no\nHost 0.0.0.0\n    StrictHostKeyChecking no\n" > ~/.ssh/config

# Versão do Hadoop — pode ser substituída em tempo de build:
#   docker build --build-arg HADOOP_VERSION=3.4.4 -f pseudo-distribuido/Dockerfile -t mapreduce-pseudo .
ARG HADOOP_VERSION=3.4.3
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xvzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} /usr/local/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Variáveis de ambiente Hadoop
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

# Regista JAVA_HOME em hadoop-env.sh (calculado dinamicamente — funciona em amd64 e arm64)
# No Hadoop 3.x, correr daemons como root requer declaração explícita das variáveis de utilizador
RUN JAVA_PATH=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "export JAVA_HOME=$JAVA_PATH"             >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_NAMENODE_USER=root"          >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_DATANODE_USER=root"          >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export YARN_RESOURCEMANAGER_USER=root"   >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export YARN_NODEMANAGER_USER=root"       >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export JAVA_HOME=$JAVA_PATH"             >> /root/.bashrc && \
    echo "export PATH=$JAVA_PATH/bin:$PATH"        >> /root/.bashrc

# Copia ficheiros de configuração Hadoop (modo pseudo-distribuído)
COPY pseudo-distribuido/config/core-site.xml  $HADOOP_HOME/etc/hadoop/core-site.xml
COPY pseudo-distribuido/config/hdfs-site.xml  $HADOOP_HOME/etc/hadoop/hdfs-site.xml
COPY pseudo-distribuido/config/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
COPY pseudo-distribuido/config/yarn-site.xml  $HADOOP_HOME/etc/hadoop/yarn-site.xml

# Formata o NameNode (cria a estrutura de metadados do HDFS)
RUN hdfs namenode -format -force

# Cria pasta de trabalho e copia ficheiros do exercício
WORKDIR /workspace
COPY colecao.txt        /workspace/
COPY colecao_grande.txt /workspace/
COPY mapper.py          /workspace/
COPY reducer.py         /workspace/
COPY pseudo-distribuido/comando.hadoop /workspace/

# Script de arranque
COPY pseudo-distribuido/start-hadoop.sh /start-hadoop.sh
RUN chmod +x /start-hadoop.sh

# Expõe as interfaces web do Hadoop
EXPOSE 9870 8088 9000

CMD ["/start-hadoop.sh"]
