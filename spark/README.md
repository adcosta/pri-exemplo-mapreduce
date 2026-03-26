# IR com Apache Spark

## Sobre este exercício

Dois notebooks PySpark que implementam os conceitos centrais de Recuperação de Informação,
partindo do índice invertido e avançando para ranking com TF-IDF e similaridade do coseno.

| Ficheiro | Descrição |
|---|---|
| `ir_spark_1_indice.ipynb` | Exercício 1 — Índice invertido (comparação com MapReduce) |
| `ir_spark_2_tfidf.ipynb` | Exercício 2 — TF-IDF e pesquisa com similaridade do coseno |
| `Dockerfile` | Container com PySpark e JupyterLab |
| `start-jupyter.sh` | Script de arranque |

Os dois exercícios são independentes e podem ser usados em sessões separadas.

---

## Como Executar

### 1. Construir a imagem

A partir da pasta `pri-exemplo-mapreduce/`:

```bash
docker build -f spark/Dockerfile -t ir-spark .
```

### 2. Iniciar o container

```bash
docker run -it -p 8888:8888 -p 4040:4040 ir-spark
```

### 3. Abrir o notebook

Navega para **http://localhost:8888** e escolhe o exercício.

Durante a execução tens também disponível:
- **http://localhost:4040** — Spark UI com o DAG de transformações e progresso dos jobs

---

## Sequência sugerida

**Exercício 1** — imediatamente a seguir ao exercício MapReduce.
Foco: perceber como o Spark funciona (RDDs, lazy evaluation, DAG).
A comparação directa com `mapper.py` e `reducer.py` é o elemento central.

**Exercício 2** — após a discussão do modelo probabilístico ou como consolidação do modelo vetorial.
Foco: implementar TF-IDF e ranking numa cadeia distribuída.
O Spark é o meio; o IR é o fim.
