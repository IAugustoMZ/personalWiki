# PySpark e Apache Kafka para Processamento de Dados em Batch e Streaming

4 notas sobre processamento distribuído de dados, ferramentas, padrões ETL e integração com bancos de dados.

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

As notas vão de `00_def_spkbst_19092025.md` a `03_def_spkbst_24092025.md`.

Voltar para [Formação Engenheiro de Dados](../README.md).
