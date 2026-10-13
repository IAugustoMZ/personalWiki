# PySpark e Apache Kafka para Processamento de Dados em Batch e Streaming

15 notas sobre processamento distribuído, operações em DataFrames, padrões ETL, integração com bancos de dados, gerenciamento de clusters, otimizações de performance, processamento em batch e streaming, engenharia de dados com PySpark, Kafka para integrações e aprendizado de máquina em tempo real.

## Tópicos cobertos

- Processamento distribuído: paralelização, resiliência, otimização de recursos, coordenação entre nós, consistência de dados, recuperação de falhas.
- PySpark: interface Python para Apache Spark, processamento distribuído em clusters, transformações de dados, armazenamento intermediário na memória, redução de I/O em disco.
- Apache Kafka: sistema distribuído de mensagens high-throughput, arquitetura produtor-consumidor, tópicos e partições, replicação e durabilidade, retenção de mensagens, Kafka Streams e Kafka Connect.
- Princípios de ETL: extração consistente de múltiplas fontes, transformações com validações e enriquecimento de dados, carregamento incremental vs full-load, automação e monitoramento, logging e tratamento de erros.
- Trabalhando com JSON e XML em Python: bibliotecas `json`, `xmltree`/`ElementTree`, `lxml`, tratamento de erros e formatação.
- Conexão com Banco de Dados usando SQLAlchemy: toolkit SQL/ORM, engine de banco de dados, string de conexão, execução de consultas diretas e com CRM, mapeamento de classes Python para tabelas, segurança de credenciais.
- Automação de Pipelines e ETL: ferramentas de orquestração (Airflow, NiFi, Luigi), scripting, containers (Docker, Kubernetes), monitoramento (Grafana, Prometheus, ELK), cloud services.
- Logging e Monitoramento de ETL: registros detalhados com timestamps e contexto, níveis de logs, centralização, rotação, estratégias de monitoramento de desempenho e qualidade.
- Erros Comuns em ETL: problemas de conexão, inconsistências de dados, performance e escalabilidade, integração de dependências, codificação, transformações, orquestração, segurança, quotas de API, infraestrutura.
- PySpark SparkSession e Transformações: schema e estrutura de dados, filter com operadores relacionais, regex_replace para limpeza, otimização de loops e memória.
- JDBC Drivers e Conexão com Bancos: Java Database Connectivity API, tipos de drivers (Bridge, Native API, Middleware, Nativo), portabilidade entre SGBDs, submissão de jobs com drivers JAR.
- Performance e Otimização de Código Python: perfilamento, estruturas de dados eficientes (numpy, sets), evitar redundâncias, programação concorrente/paralela, caching, gestão de memória, Cython/Numba.
- Operações Avançadas em PySpark (Parte I): tipos de dados complexos (Array vs Map), método collect() para trazer dados ao driver, withColumn para derivar colunas, operações aritméticas/strings/data-hora, funções de agregação, UDFs, MapType para pares chave-valor.
- RDD vs DataFrame e Operações Distribuídas (Parte II): abstração RDD (imutável, particionado, controle fino) vs DataFrame (alto nível, otimização automática), particionamento strategies (hash, range), repartition() vs coalesce(), time operations, window functions (rank, lag, lead, quantis).
- Armazenamento Distribuído e Cluster Spark (Parte III): conceitos de distributed storage (redundância, escalabilidade, acesso concorrente), modos de gerenciamento do cluster (Standalone, YARN, Mesos, Kubernetes), componentes YARN (Resource Manager, Node Manager), alocação dinâmica, vantagens do Spark.
- Instalação e Configuração Multi-Node Cluster Spark e HDFS (Parte IV): big data processing (ETL/ELT), análise em tempo real, ML/AI em escala, graph processing, consultas/agregações, integração de dados, benefícios conjuntos Spark+HDFS+YARN (escalabilidade, resiliência, gerenciamento de recursos, flexibilidade).
- PySpark para Processamento Distribuído em Batch (Parte I): conceito de batch processing (dados coletados em blocos, eficiência para grandes volumes), limpeza e tratamento de dados faltantes (remoção de linhas, preenchimento, interpolação, uso de indicadores), normalização para reduzir redundância e melhorar integridade, desnormalização para consultas mais rápidas.
- Particionamento de Dados e Engenharia de Atributos (Parte II): estratégias de particionamento (por coluna, dinâmico, bucketing, hierárquico, intervalos de valores, combinado) para melhorar performance de consultas; engenharia de atributos para transformar dados brutos em features para ML; ajuste do número de partições para balancear paralelização e gerenciamento.
- Processamento de Streaming e Machine Learning em Tempo Real: processamento contínuo de dados de múltiplas fontes com baixa latência (sem armazenamento intermediário), detecção de anomalias, monitoramento em tempo real; integração de ML/Deep Learning com streaming (CNN, RNN) para reconhecimento facial e análise de sentimentos; arquitetura de Autoencoder (encoder-decoder) para compressão e redução de dimensionalidade de dados.
- PySpark Streaming Fundamentals (Parte I): DStream & micro-batches, receivers, window operations, stateful operations, checkpointing; data cleaning & treatment (filtragem, deduplicação, normalização), windowed operations, stateful processing (updateStateByKey, mapWithState), data persistence (databases, data lakes, HDFS, Kafka, Elasticsearch), integration with external sources (Kafka, Kinesis, files, databases, sockets), monitoring/debugging, backpressure & rate limiting.
- Multi-Node Cluster Spark, HDFS e Kafka (Parte II): quando usar Apache Kafka (real-time pipelines, low-latency systems, event processing, data integration, IoT workloads, microsserviços), arquitetura Kafka (Producer, Consumer, Broker, Zookeeper/Kafka Controller), gerenciamento de coordenação, balanceamento de carga.

As notas vão de `00_def_spkbst_19092025.md` a `14_def_spkbst_02112025.md`.

Voltar para [Formação Engenheiro de Dados](../README.md).
