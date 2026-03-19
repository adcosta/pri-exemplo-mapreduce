# Índice Invertido com MapReduce

## Sobre este projeto

Este exercício demonstra como construir um **índice invertido** — a estrutura de dados central em sistemas de **Recuperação de Informação (IR)** — usando o modelo MapReduce com Hadoop Streaming.

O ambiente de execução é um container Docker com Hadoop instalado. Os scripts de Map e Reduce são escritos em Python e recebem uma pequena coleção de documentos como entrada.

| Ficheiro | Descrição |
|---|---|
| `mapper.py` | Fase Map — tokeniza cada documento e emite pares `(termo, doc_id)` |
| `reducer.py` | Fase Reduce — agrega os `doc_id` por termo e produz o índice invertido |
| `colecao.txt` | Coleção de 4 documentos de exemplo no formato `doc_id<TAB>texto` |
| `comando.hadoop` | Comando Hadoop Streaming para executar o job no cluster |
| `Dockerfile` | Definição do container com Hadoop 3.4.3 |

---

## Como Executar

### 1. Construir a imagem Docker

```bash
docker build -t mapreduce-ir .
```

### 2. Iniciar o container

```bash
docker run -it mapreduce-ir
```

O container abre uma shell interativa no diretório `/workspace`, onde todos os ficheiros do projeto estão disponíveis.

### 3. Testar localmente com pipes Unix

A forma mais rápida de verificar a lógica dos scripts, sem precisar de Hadoop a correr:

```bash
cat colecao.txt | python3 mapper.py | sort | python3 reducer.py
```

> Ver a secção [Teste Local sem Hadoop](#teste-local-sem-hadoop) para mais detalhes.

### 4. Executar com Hadoop Streaming (modo local)

```bash
bash comando.hadoop
```

O script copia a coleção para um directório de input local, executa o job com Hadoop Streaming e imprime o índice invertido no terminal. Não requer HDFS nem YARN — o Hadoop usa o sistema de ficheiros local por defeito (modo standalone).

---

## Introdução ao MapReduce

MapReduce é um modelo de programação e um framework de execução desenvolvido pela Google em 2004 para **processar grandes volumes de dados** de forma eficiente em sistemas distribuídos.

- Inspirado em conceitos de programação funcional **map** e **reduce**.
- Permite **processamento paralelo** em milhares de máquinas.
- Utilizado para processar **big data** de forma automatizada e escalável.

_Referência: Dean & Ghemawat, 2004_

---

## Motivação para o MapReduce

**Porque foi necessário criar o MapReduce?**
- O processamento de grandes volumes de dados era difícil e caro.
- As abordagens existentes de computação paralela eram complexas e exigiam gestão manual de falhas.
- Necessidade de um modelo de programação **tolerante a falhas**, **escalável** e **simples**.

**Principais Problemas Resolvidos:**
- Paralelização e balanceamento de carga automáticos  
- Tolerância a falhas e recuperação automática  
- API simples para cálculos complexos  
- Processamento eficiente com **execução otimizada pela localização dos dados**

---

## O Modelo MapReduce

**Fluxo de Trabalho Básico:**
1. **Fase de Map:** Processa os dados de entrada e gera pares chave-valor.
2. **Shuffle & Sort:** Agrupa os dados por chave e distribui-os pelos reducers.
3. **Fase de Reduce:** Agrega e processa os dados, produzindo a saída final.

Exemplo: **Contagem de Palavras**
| Passo | Entrada | Saída |
|------|-------|--------|
| **Map** | "Olá mundo. Olá Hadoop." | ("Olá", 1), ("mundo", 1), ("Olá", 1), ("Hadoop", 1) |
| **Shuffle & Sort** | Saída do mapeamento | ("Olá", [1, 1]), ("mundo", [1]), ("Hadoop", [1]) |
| **Reduce** | ("Olá", [1, 1]) → 2 | ("Olá", 2), ("mundo", 1), ("Hadoop", 1) |

---

## Arquitetura do Sistema
**Como o MapReduce executa tarefas?**
- **Nó Mestre:** Coordena a execução dos jobs.
- **Nós Trabalhadores:** Executam tarefas de mapeamento e redução em paralelo.
- **Sistema de Ficheiros Distribuído (HDFS/GFS):** Armazena os dados de entrada e saída de forma eficiente.

Garantias:
- **Tolerância a falhas automática**: Tarefas falhadas são **reexecutadas** noutro nó.
- **Otimização pela localização dos dados**: Move a computação **para onde os dados estão armazenados**.

---

## Principais Características e Vantagens

- **Simplicidade**: Os programadores só precisam de escrever as funções **Map** & **Reduce**.  
- **Paralelização automática**: Distribui o trabalho por múltiplos nós.  
- **Escalabilidade**: Funciona eficientemente com petabytes de dados.  
- **Tolerância a falhas**: Lida automaticamente com falhas de máquinas.  
- **Desempenho elevado**: Os dados são processados localmente sempre que possível.  

_Utilizadores de Exemplo: Google, Yahoo, Facebook, Twitter, Apache Hadoop_

---

## Limitações do MapReduce
- **Processamento em Lote**: Não é adequado para aplicações em tempo real.  
- **Sobrecarga de I/O em Disco**: Leituras e escritas frequentes tornam a execução mais lenta.  
- **Dificuldade em Expressar Certos Algoritmos**: Computações iterativas (ex.: Machine Learning) exigem múltiplos jobs MapReduce.  
- **Substituído por Frameworks Mais Avançados**: Spark, Flink e outros lidam melhor com processamento em memória.

---

## Evolução para Além do MapReduce
- **Apache Hadoop**: Implementação open-source do MapReduce.  
- **Apache Spark**: Melhor desempenho ao **manter os dados em memória** (100x mais rápido).  
- **Apache Flink & Google Dataflow**: Modelos de processamento em streaming e tempo real.  

**O MapReduce lançou as bases para os frameworks modernos de big data!**

---

## Teste Local sem Hadoop

Antes de executar o job no Hadoop, é possível simular o pipeline MapReduce localmente com pipes Unix. Isto é útil para verificar a lógica dos scripts sem precisar de um cluster a funcionar.

```bash
cat colecao.txt | python3 mapper.py | sort | python3 reducer.py
```

Cada fase corresponde a uma etapa do MapReduce:

| Comando | Fase MapReduce |
|---------|----------------|
| `cat colecao.txt` | Leitura dos dados de entrada |
| `python3 mapper.py` | Fase **Map** — emite pares `(termo, doc_id)` |
| `sort` | **Shuffle & Sort** — agrupa por chave (termo) |
| `python3 reducer.py` | Fase **Reduce** — constrói o índice invertido |

O resultado esperado é o índice invertido, com cada termo seguido dos documentos onde aparece:

```
busca     Doc3
construir Doc4
eficiente Doc1
exemplo   Doc4
...
```

> **Nota:** o `sort` aqui substitui manualmente o Shuffle & Sort que o Hadoop faz automaticamente entre o Map e o Reduce.

---

## Resumo e Conclusão

- **O MapReduce revolucionou o processamento de big data** ao introduzir um modelo de programação simples, escalável e tolerante a falhas.
- Embora o **processamento em lote ainda seja usado**, frameworks mais modernos **(como Spark)** oferecem melhor desempenho para análises em tempo real.
-  O MapReduce continua a ser **importante historicamente** como a base do **Hadoop** e do ecossistema moderno de big data.

_Referência: "MapReduce: Simplified Data Processing on Large Clusters" – Dean & Ghemawat, 2004_

---

## Sugestões de Extensão

### 1. Frequência de termos (TF)

O `reducer.py` atual regista apenas **quais documentos** contêm cada termo (usando um `set`). Uma extensão natural é contar **quantas vezes** cada termo aparece em cada documento — a chamada *term frequency* (TF), que é a base do modelo TF-IDF usado em sistemas IR reais.

O output passaria de:
```
ir    ['Doc1', 'Doc2', 'Doc3']
```
para:
```
ir    {'Doc1': 1, 'Doc2': 1, 'Doc3': 1}
```

**Pista:** o mapper já emite um par `(palavra, doc_id)` por cada ocorrência. No reducer, em vez de adicionar `doc_id` a um `set`, mantém um dicionário `{doc_id: contagem}` e incrementa o contador a cada linha com o mesmo `doc_id`.

### 2. Remoção de stopwords

Palavras funcionais como `a`, `em`, `para`, `um` aparecem no índice mas têm pouco valor discriminativo para pesquisa. Experimenta filtrar estas palavras no mapper antes de emitir o par `(palavra, doc_id)`.

### 3. Normalização de acentos

No índice atual, `indice` e `índice` são termos diferentes. Num sistema IR real aplicar-se-ia normalização de caracteres Unicode para os colapsar num único termo. A biblioteca `unicodedata` do Python pode ajudar.

---

