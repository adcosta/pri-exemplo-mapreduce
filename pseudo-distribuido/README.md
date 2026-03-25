# Modos de Execução do Hadoop

O Hadoop pode ser executado em três modos distintos, com complexidade e fidelidade crescentes ao ambiente de produção.

---

## Modo 1 — Local (Standalone)

Este é o modo por defeito quando não existe nenhum ficheiro de configuração. O Hadoop corre como um único processo Java na máquina local e usa o sistema de ficheiros local (não o HDFS).

**Características:**
- Sem daemons (sem NameNode, DataNode, ResourceManager, etc.)
- Input e output são directorias locais
- Sem HDFS: `hdfs dfs` opera sobre o sistema de ficheiros local
- Útil para desenvolver e testar a lógica de mapper e reducer

**Quando usar:** para aprender a escrever e depurar jobs MapReduce sem overhead de configuração. É o modo usado no exercício principal deste repositório.

**Comando típico:**
```bash
hadoop jar hadoop-streaming-*.jar \
    -input  input/colecao.txt \
    -output output/resultado \
    -mapper  "python3 mapper.py" \
    -reducer "python3 reducer.py"
```

---

## Modo 2 — Pseudo-distribuído

O Hadoop corre todos os seus daemons numa única máquina, mas cada daemon corre num processo Java separado, tal como aconteceria num cluster real. O HDFS e o YARN estão activos.

**Características:**
- NameNode e DataNode correm em separado (HDFS real)
- ResourceManager e NodeManager activos (YARN real)
- Requer SSH sem password para localhost
- Interfaces web disponíveis: HDFS (`localhost:9870`) e YARN (`localhost:8088`)
- Os ficheiros de input e output residem no HDFS, não no sistema de ficheiros local

**Quando usar:** para simular um cluster real numa única máquina. Os alunos ganham exposição ao HDFS, aos comandos `hdfs dfs`, ao ciclo de vida de um job no YARN, e às interfaces de monitorização.

**Diferença fundamental face ao modo local:** os dados estão no HDFS e os jobs são geridos pelo YARN. O fluxo de trabalho passa a incluir:
```bash
hdfs dfs -put ficheiro.txt /caminho/hdfs/
hadoop jar hadoop-streaming-*.jar -input /caminho/hdfs/... -output /hdfs/output/...
hdfs dfs -cat /hdfs/output/part-00000
```

---

## Modo 3 — Totalmente distribuído

O Hadoop corre em múltiplas máquinas físicas ou virtuais, cada uma com o seu conjunto de daemons. É o modo de produção.

**Características:**
- NameNode(s) e DataNodes em máquinas separadas
- ResourceManager e NodeManagers em máquinas separadas
- Elevada tolerância a falhas e escalabilidade real
- Configuração envolve gestão de chaves SSH entre nós, ficheiros `workers`, e tuning de memória/CPU por nó

**Quando usar:** em produção ou em laboratórios de cluster reais (ex.: ambientes com vários VMs ou serviços cloud como Amazon EMR ou Google Dataproc).

---

## Comparação resumida

| Característica         | Local        | Pseudo-distribuído | Totalmente distribuído |
|------------------------|:------------:|:------------------:|:----------------------:|
| Nº de máquinas         | 1            | 1                  | ≥ 3                   |
| Processos Java         | 1            | vários             | vários por máquina    |
| HDFS activo            | Não          | Sim                | Sim                   |
| YARN activo            | Não          | Sim                | Sim                   |
| SSH necessário         | Não          | Sim                | Sim                   |
| Tolerância a falhas    | Não          | Parcial            | Sim                   |
| Adequado para          | Testes locais | Aprendizagem       | Produção              |

---

## Configuração do modo pseudo-distribuído

O modo pseudo-distribuído requer quatro ficheiros XML em `$HADOOP_HOME/etc/hadoop/` e SSH configurado sem password.

### SSH sem password

O Hadoop usa SSH para iniciar os daemons (mesmo em localhost). É necessário gerar um par de chaves e autorizar o acesso:

```bash
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```

### core-site.xml — sistema de ficheiros por defeito

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

### hdfs-site.xml — configuração do HDFS

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### mapred-site.xml — framework de execução MapReduce

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

### yarn-site.xml — configuração do YARN

```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

### Arranque e paragem dos serviços

```bash
# Formatar o NameNode (apenas na primeira vez)
hdfs namenode -format

# Iniciar HDFS
start-dfs.sh

# Iniciar YARN
start-yarn.sh

# Verificar que os daemons estão a correr
jps

# Parar tudo
stop-yarn.sh
stop-dfs.sh
```

O comando `jps` deve listar: `NameNode`, `DataNode`, `SecondaryNameNode`, `ResourceManager`, `NodeManager`.

---

## Como construir e correr o container pseudo-distribuído

O Dockerfile deste directório configura automaticamente tudo o que foi descrito acima. É construído a partir da pasta pai para ter acesso aos ficheiros do exercício:

```bash
# A partir da pasta pri-exemplo-mapreduce/
docker build -f pseudo-distribuido/Dockerfile -t mapreduce-pseudo .
```

### Iniciar o container com hostname fixo

O Hadoop gera links internos usando o hostname do container. Sem um hostname fixo, o hostname é o ID do container (ex: `b0c5e563ebea`), o que torna os links das interfaces web inacessíveis a partir do browser.

A solução é dar um nome fixo ao container com `--hostname` e registá-lo no `/etc/hosts` da máquina:

**1. Adicionar ao `/etc/hosts` da tua máquina** (apenas uma vez):
```
127.0.0.1   hadoop-local
```

**2. Iniciar o container com esse hostname:**
```bash
docker run -it \
  -p 9870:9870 \
  -p 9868:9868 \
  -p 9864:9864 \
  -p 8088:8088 \
  -p 8042:8042 \
  -p 19888:19888 \
  --hostname hadoop-local \
  mapreduce-pseudo
```

Após o arranque, o container fica com uma shell activa em `/workspace`. Para executar o job:

```bash
bash comando.hadoop
```

As interfaces web ficam acessíveis no browser em:

| Interface | URL | Daemon |
|---|---|---|
| HDFS NameNode | http://localhost:9870 | NameNode |
| SecondaryNameNode | http://hadoop-local:9868 | SecondaryNameNode |
| DataNode | http://hadoop-local:9864 | DataNode |
| YARN ResourceManager | http://localhost:8088 | ResourceManager |
| NodeManager | http://hadoop-local:8042 | NodeManager |
| JobHistory Server | http://hadoop-local:19888 | MapReduce JobHistory |
