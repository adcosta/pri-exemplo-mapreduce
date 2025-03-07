*MapReduce: Processamento Simplificado de Dados em Grandes Clusters*

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

## Resumo e Conclusão

- **O MapReduce revolucionou o processamento de big data** ao introduzir um modelo de programação simples, escalável e tolerante a falhas.
- Embora o **processamento em lote ainda seja usado**, frameworks mais modernos **(como Spark)** oferecem melhor desempenho para análises em tempo real.
-  O MapReduce continua a ser **importante historicamente** como a base do **Hadoop** e do ecossistema moderno de big data.

_Referência: "MapReduce: Simplified Data Processing on Large Clusters" – Dean & Ghemawat, 2004_

---

