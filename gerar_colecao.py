import random

random.seed(42)

# Blocos de texto temáticos sobre IR, MapReduce, motores de busca, etc.
# Cada bloco é uma frase ou fragmento que pode ser combinado

frases_ir = [
    "a recuperação de informação estuda como encontrar documentos relevantes numa coleção",
    "um índice invertido mapeia cada termo para os documentos onde esse termo aparece",
    "a relevância de um documento é medida pela sua proximidade ao query do utilizador",
    "o modelo vetorial representa documentos e queries como vetores num espaço de termos",
    "o modelo booleano usa operadores AND OR NOT para combinar termos de pesquisa",
    "o modelo probabilístico estima a probabilidade de um documento ser relevante para um query",
    "a precisão mede a fração de documentos recuperados que são de facto relevantes",
    "o recall mede a fração de documentos relevantes que foram de facto recuperados",
    "a medida F1 combina precisão e recall numa única métrica de avaliação",
    "a stemming reduz palavras à sua forma raiz para melhorar o matching de termos",
    "a lematização converte palavras para a sua forma canónica considerando contexto gramatical",
    "as stopwords são palavras muito frequentes com pouco valor discriminativo para a pesquisa",
    "o TF-IDF pondera a frequência de um termo no documento e a sua raridade na coleção",
    "a term frequency mede quantas vezes um termo aparece num determinado documento",
    "o inverse document frequency penaliza termos que aparecem em muitos documentos",
    "o BM25 é uma função de ranking baseada em TF-IDF com saturação da frequência de termos",
    "o PageRank mede a importância de uma página web com base nos links que apontam para ela",
    "a análise de âncoras de hiperlinks melhora a qualidade do ranking em motores de busca web",
    "o crawler é o componente do motor de busca que percorre a web e descarrega páginas",
    "o índice invertido é construído a partir do conteúdo das páginas recolhidas pelo crawler",
    "a compressão do índice reduz o espaço em disco necessário para armazenar listas de postings",
    "as listas de postings contêm os identificadores dos documentos que contêm cada termo",
    "o merge de índices combina índices parciais construídos em paralelo num índice final",
    "a busca por frase requer informação de posição nas listas de postings do índice",
    "a expansão de query adiciona termos relacionados para aumentar o recall da pesquisa",
    "o feedback de relevância usa documentos marcados como relevantes para reformular o query",
    "o modelo de linguagem estima a probabilidade de um query ter sido gerado por um documento",
    "a sumarização automática extrai as frases mais informativas de um documento",
    "a classificação de texto atribui categorias predefinidas a documentos com base no conteúdo",
    "o clustering agrupa documentos similares sem categorias predefinidas",
]

frases_mapreduce = [
    "o MapReduce divide o processamento de dados em duas fases map e reduce",
    "a fase map processa cada registo de entrada e emite pares chave valor",
    "a fase reduce agrega todos os valores associados à mesma chave",
    "o shuffle and sort transfere e ordena os pares chave valor entre mappers e reducers",
    "o Hadoop é a implementação open source do MapReduce desenvolvida pela Apache",
    "o HDFS distribui os dados em blocos por múltiplos nós do cluster",
    "o NameNode gere os metadados do sistema de ficheiros distribuído HDFS",
    "o DataNode armazena os blocos de dados e reporta ao NameNode periodicamente",
    "o YARN gere os recursos do cluster e escala os jobs MapReduce pelos nós",
    "o ResourceManager do YARN atribui containers aos jobs submetidos ao cluster",
    "o NodeManager executa as tarefas map e reduce nos nós worker do cluster",
    "a tolerância a falhas do Hadoop reinicia tarefas falhadas noutros nós automaticamente",
    "o Hadoop Streaming permite usar qualquer programa como mapper ou reducer",
    "o combiner é um mini-reducer local que reduz o volume de dados no shuffle",
    "o partitioner decide qual reducer recebe cada par chave valor emitido pelo mapper",
    "o número de reducers afeta o número de ficheiros de output e o desempenho do job",
    "o Hadoop usa localidade dos dados para executar mappers nos nós onde os dados residem",
    "os jobs MapReduce são adequados para processamento em lote de grandes volumes de dados",
    "o MapReduce não é adequado para processamento iterativo como algoritmos de machine learning",
    "o Apache Spark supera o MapReduce ao manter dados intermédios em memória",
    "o Spark usa RDDs resilient distributed datasets como abstração fundamental de dados",
    "o DAG do Spark otimiza a sequência de transformações antes de as executar",
    "o Spark Streaming processa dados em micro-batches em tempo quasi-real",
    "o Apache Flink processa dados em streaming com latência muito baixa",
    "o Hive traduz queries SQL em jobs MapReduce para análise de dados em HDFS",
    "o Pig usa uma linguagem de fluxo de dados chamada Pig Latin para definir pipelines",
    "o HBase é uma base de dados NoSQL distribuída construída sobre o HDFS",
    "o ZooKeeper coordena serviços distribuídos e fornece configuração centralizada",
    "o Oozie é um sistema de workflow para orquestrar jobs Hadoop",
    "o Sqoop transfere dados entre bases de dados relacionais e o HDFS",
]

frases_sistemas = [
    "o Google foi o primeiro motor de busca a usar PageRank como sinal de ranking",
    "o índice do Google processa centenas de biliões de páginas web",
    "a Lucene é a biblioteca de indexação e pesquisa open source mais usada",
    "o Elasticsearch é construído sobre a Lucene e fornece pesquisa distribuída via REST API",
    "o Solr é outro sistema de pesquisa construído sobre a Lucene com foco em faceting",
    "o Whoosh é uma biblioteca de pesquisa leve implementada em Python puro",
    "os sistemas de recomendação usam técnicas de IR para sugerir itens relevantes",
    "a filtragem colaborativa recomenda itens com base em utilizadores similares",
    "a filtragem baseada em conteúdo recomenda itens similares aos que o utilizador gostou",
    "o processamento de linguagem natural melhora a compreensão de queries em linguagem natural",
    "a entidade nomeada reconhece nomes de pessoas lugares e organizações no texto",
    "a análise de sentimento classifica o sentimento positivo negativo ou neutro de um texto",
    "os word embeddings representam palavras como vetores densos num espaço semântico",
    "o word2vec aprende representações de palavras a partir de co-ocorrências em texto",
    "o BERT usa atenção bidirecional para criar representações contextuais de palavras",
    "os transformers revolucionaram o processamento de linguagem natural desde 2017",
    "a recuperação densa usa embeddings neurais para encontrar documentos semanticamente similares",
    "o retrieval augmented generation combina pesquisa com geração de linguagem natural",
    "os large language models são usados para reranking e sumarização em sistemas IR modernos",
    "a avaliação de sistemas IR usa coleções de teste com queries e julgamentos de relevância",
    "o TREC Text Retrieval Conference é a principal conferência de avaliação de sistemas IR",
    "as métricas de avaliação incluem MAP mean average precision NDCG e MRR",
    "o crawling respeitoso respeita o ficheiro robots txt e os limites de taxa dos servidores",
    "a deduplicação remove páginas duplicadas ou quase duplicadas do índice",
    "o link spam tenta manipular o PageRank criando redes artificiais de hiperlinks",
    "a pesquisa semântica tenta compreender a intenção por trás de um query",
    "a pesquisa por voz requer transcrição de fala e compreensão de linguagem natural",
    "a pesquisa de imagens usa descritores visuais ou texto alternativo para indexação",
    "os sistemas de perguntas e respostas localizam a resposta exata a uma questão no texto",
    "a extração de informação identifica factos estruturados em texto não estruturado",
]

todos_fragmentos = frases_ir + frases_mapreduce + frases_sistemas

documentos = []
for i in range(1, 101):
    doc_id = f"Doc{i:03d}"
    # Cada documento é composto por 3 a 6 frases aleatórias
    n_frases = random.randint(3, 6)
    frases = random.sample(todos_fragmentos, n_frases)
    texto = " ".join(frases)
    documentos.append(f"{doc_id}\t{texto}")

with open("colecao_grande.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(documentos) + "\n")

print(f"Gerados {len(documentos)} documentos.")
print("Primeiros 3:")
for d in documentos[:3]:
    print(d[:120] + "...")
