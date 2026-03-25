#!/bin/bash
# Script de arranque do Hadoop em modo pseudo-distribuído

set -e

echo ">>> A iniciar SSH (necessário para o Hadoop arrancar os daemons)..."
service ssh start

echo ">>> A iniciar HDFS (NameNode + DataNode)..."
start-dfs.sh

echo ">>> A iniciar YARN (ResourceManager + NodeManager)..."
start-yarn.sh

echo ">>> A aguardar que os serviços estabilizem..."
sleep 6

echo ">>> A criar estrutura de directórios no HDFS..."
hdfs dfs -mkdir -p /user/root
hdfs dfs -mkdir -p /workspace/input

echo ">>> A copiar coleções para HDFS..."
hdfs dfs -put /workspace/colecao.txt        /workspace/input/colecao.txt
hdfs dfs -put /workspace/colecao_grande.txt /workspace/input/colecao_grande.txt

echo ""
echo "========================================================"
echo "  Hadoop pseudo-distribuído está a correr."
echo ""
echo "  Interface HDFS NameNode : http://localhost:9870"
echo "  Interface YARN           : http://localhost:8088"
echo ""
echo "  Para executar o job MapReduce:"
echo "    bash /workspace/comando.hadoop"
echo "========================================================"
echo ""

# Mantém o container em execução com uma shell interactiva
exec bash
