#!/bin/bash
# Define JAVA_HOME dinamicamente (funciona em amd64 e arm64)
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
export PYSPARK_PYTHON=python3

echo "========================================================"
echo "  PySpark + JupyterLab"
echo "  Spark UI : http://localhost:4040  (durante execução)"
echo "  Notebook : http://localhost:8888"
echo "========================================================"

jupyter lab \
  --ip=0.0.0.0 \
  --port=8888 \
  --no-browser \
  --allow-root \
  --ServerApp.token='' \
  --ServerApp.password=''
