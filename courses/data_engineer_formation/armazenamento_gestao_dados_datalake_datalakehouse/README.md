# Armazenamento e Gestão de Dados com Datalake e Datalakehouse

30 notas sobre arquitetura de armazenamento de dados: diferenças entre Data Lake e Data Lakehouse, evolução dos conceitos, componentes e arquiteturas de referência, segurança/privacidade, ferramentas de mercado, planejamento de custos (on-premises, nuvem e análise comparativa), futuro tecnológico, metodologia de implementação ágil, design/implementação prática de Data Lakes locais com camadas de armazenamento e processamento distribuído, segurança operacional, performance, backup/recuperação, ferramentas de gerenciamento, design de solução com Terraform e automação, otimização/escalabilidade com gerenciamento de custos, governança com linhagem/observabilidade/qualidade, enriquecimento de dados com documentação e metadados, convergência entre Data Lakes e Data Lakehouses (arquitetura, vantagens, design), segurança e governança em Data Lakehouse (RBAC, criptografia, auditoria, catálogo de dados), introdução à plataforma Databricks (workspace, notebooks, data ingestion, workflows, Delta Live Tables, clean rooms), Delta Live Tables vs Delta Lake, operações CRUD em Delta Lake, time travel, segurança com Delta Lake, e introdução a pipelines ETL com camadas Bronze/Silver/Gold.

## Tópicos cobertos

- Comparação entre Datalake e Datalakehouse: flexibilidade, escalabilidade, governança e desempenho de consultas.
- Data Stack: fontes de dados, pipelines e ETL, armazenamento centralizado, plataformas de análise e processamento, BI e visualização, machine learning e IA, governança e segurança dos dados.
- Conceito e evolução de Data Warehouse, Data Lake e Data Lakehouse: da infraestrutura on-premises à nuvem, e a tendência de convergência entre Data Lakes e Data Warehouses.
- Componentes-chave, benefícios e desafios de Data Lakes; comparação entre Data Warehouse, Data Lake, arquitetura de dois níveis e Datalakehouse (com diagrama de swim lanes).
- Casos de uso de Data Lakehouses, segurança/privacidade (RBAC, criptografia, auditoria, LGPD) e ferramentas de mercado para Data Lake e Data Lakehouse.
- Planejamento de custos (CAPEX/OPEX) para Data Lake on-premises, Data Lake em nuvem e Data Lakehouse avançado em nuvem, com análise de custos de hardware, software, manutenção e recursos humanos por cenário; comparativo de custo total e por TB; apresentação de orçamento para tomadores de decisão.
- Futuro de Data Lakes e Data Lakehouses: tendências tecnológicas (IA/ML, eficiência de consulta, interoperabilidade), regulamentação (GDPR/LGPD), automação e self-service, sustentabilidade.
- Construção eficiente de Data Lakes: 4 estágios (landing zone, data science environment, offload para DW, operações críticas) e abordagem ágil iterativa com foco em valor de negócio e feedback contínuo.
- Planejamento e design de Data Lakes on-premises: 6 etapas (avaliação de requisitos, arquitetura/design, infraestrutura, implementação/integração, monitoramento, adaptação/escalabilidade); implementação prática com Hadoop+Spark em Docker Desktop (5 VMs, YARN, SSH).
- Implementação de camadas de armazenamento e processamento distribuído: carregamento de dados em HDFS (hdfs dfs commands), scripts PySpark com spark-submit, processamento em memória distribuída, particionamento de dados e pipelines de transformação.
- Monitoramento, segurança operacional, performance e manutenção: acompanhamento via YARN/HDFS/History Server; autenticação/autorização (RBAC); políticas de segurança, criptografia, auditoria; otimização (particionamento, indexação, caching, query optimization); backup/recuperação automatizado; ferramentas de gerenciamento (AWS Lake Formation, Azure Data Lake, GCP Dataproc, Cloudera, Databricks, CloudWatch, Splunk, Prometheus/Grafana, ELK Stack).
- Design de solução para Data Lake/Lakehouse em nuvem: planejamento arquitetônico (requisitos, plataforma, design), Infraestrutura como Código com Terraform (modularidade, gerenciamento de estado), implementação de segurança (IAM, criptografia, auditoria), integração e automação com CI/CD e data pipelines, monitoramento/otimização de custos, documentação e treinamento.
- IAM roles e access keys para segurança de acesso; otimização e escalabilidade (desacoplamento, auto-scaling, metadados, data pipelines); monitoramento e gerenciamento de custos (CloudWatch, CloudTrail, Config, Cost Explorer, Budgets, classes de armazenamento, Instâncias Reservadas); estratégia de backup/recuperação (automatização, versionamento, replicação cross-region, RTO/RPO, AWS Elastic Disaster Recovery, PITR).
- Linhagem de dados (data lineage) para rastreabilidade e conformidade regulatória (GDPR/LGPD); ferramentas (Apache Atlas, Collibra, Talend, Informatica); observabilidade em Data Lake (coleta abrangente, monitoramento real-time, alertas, visualização, correlação e contexto com Kafka, Prometheus, Grafana, Kibana, Elastic Stack, Datadog); monitoramento e alertas (Prometheus, Grafana, ELK, PagerDuty, Slack, Opsgenie); qualidade de dados com 5 dimensões (precisão, completude, consistência, relevância, atualidade).
- Estratégia para qualidade de dados: políticas, conselho de governança, automatização de validação/limpeza (ETL, ML), cultura organizacional, monitoramento contínuo. Governança de dados: definição, benefícios (qualidade, conformidade, eficiência), implementação de políticas e controles (conselho, documentação, treinamento), controles de acesso/segurança (MFA, IAM, criptografia), monitoramento/auditoria, gestão de qualidade. Ferramentas: Collibra, Informatica Axon, Alation (AI-driven), Talend Data Fabric.
- Enriquecimento de dados: processo de melhorar qualidade/utilidade adicionando contexto (APIs públicas, dados comerciais, ML/IA); casos de uso (segmentação de clientes, finanças/seguros, manufatura/logística, governo, P&D); ferramentas boto3 para AWS, hash/SHA-256 para linhagem, observabilidade via snapshots/estatísticas, qualidade baseada em regras de negócio, mascaramento de dados (substituição, embaralhamento, truncamento, criptografia) para privacidade/segurança, automação com bash scripts e Grafana. Documentação e metadados: arquitetura, objetivos, fontes, formatos, transformações, políticas; metadados descrevem características (origem, estrutura, esquema, contexto, acesso) para descoberta e conformidade.
- Convergência entre Data Lakes e Data Lakehouses: plataforma unificada combinando flexibilidade, escalabilidade e governança; vantagens (simplicidade, suporte a dados estruturados/não-estruturados, desempenho, custos reduzidos, escalabilidade, governança unificada); camadas de armazenamento (escalável, econômico em nuvem), camada de processamento (Apache Spark, query engines), e camada de governança (metadados, catálogos, controles de acesso).
- Segurança e Governança em Data Lakehouse: controle de acesso baseado em funções (RBAC), criptografia de dados (em repouso e em trânsito com TLS), auditoria e monitoramento de acessos/consultas, isolamento de rede (VPN, firewalls), gestão de identidades e chaves (OAuth, MFA); governança federada com políticas regionais e padrões globais; catálogo de dados centralizado (Apache Atlas, AWS Glue) com esquemas, descrições e metadados.
- Plataforma Databricks: data lakehouse unificada baseada em Apache Spark com suporte a dados estruturados e não-estruturados; workspace com notebooks (Python, Scala, SQL, R), jobs e workflows, integrações via conectores de ingestão, dashboards e consultas; clean rooms para processamento seguro apontando para armazenamento externo sem upload de dados; Delta Live Tables para criação declarativa e otimizada de pipelines de dados contínuos ou em lotes com rastreamento de linhagem; catalog com suporte a busca vetorial; monitoramento e execução de jobs em workflows.
- Pipelines com Delta Live Tables em Databricks: integração de dados via Airbyte (autenticação OAuth/PAT, sincronização full refresh/incremental com append/overwrite/dedup, cursor para tracking incremental); carregamento manual para casos pontuais; suporte multilíngue (Python, Scala, SQL, R) e Databricks Connect para IDEs (VS Code, PyCharm, RStudio, IntelliJ); SQL Warehouse para execução SQL-only; notebooks com cluster Spark em nuvem, resultados intermediários em memória; gráficos com pySpark+matplotlib; DataFrame Spark otimizado para ambientes distribuídos; auto-shutdown para economia; costs menores que infraestrutura equivalente.
- Fundamentos de Delta Lake: camada de armazenamento código aberto baseada em Apache Spark; características (transações ACID, versionamento com time travel, esquema evolutivo, gerenciamento tabular, performance com índices/compactação, compatibilidade com Parquet); princípios ACID (Atomicidade, Consistência, Isolamento, Durabilidade); arquitetura (camada de dados com Parquet, logs de transações JSON com snapshots, catálogo de metadados, integração com Spark, otimizações de leitura/escrita, interação com ferramentas de análise).
- Fluxo de operações em Delta Lake: ingestão (CSV, JSON, Parquet, APIs), conversão para tabelas Delta com metadados e logs, armazenamento com ACID, operações de leitura/escrita com consistência e snapshots, otimização (compactação, particionamento, vaccum), consulta e análise sem duplicação. Otimizações: compactação de arquivos, particionamento por colunas filtro, vaccum para limpeza, manutenção de índices/estatísticas, esquema evolutivo; otimizações de query: data skipping, optimize para reorganização, streaming incremental, caching, time travel, suporte a Spark Analyzer Optimizer.
- Delta Live Tables vs Delta Lake: DLT como funcionalidade Databricks para pipelines declarativos automatizados; Delta Lake como framework open source de armazenamento agnóstico. Operações CRUD em Delta Lake (CREATE/INSERT, READ/SELECT, UPDATE com condition/set, DELETE). Time Travel: acesso a versões anteriores via timestamps/version numbers, auditoria, debugging, recuperação de dados (VACCUM com política de retenção). Segurança e Governança: controle de acesso IAM e RBAC, auditoria via logs de transações, time travel para análise retrospectiva, validação de qualidade de dados, políticas de retenção e limpeza, criptografia em repouso e em trânsito.
- Pipeline ETL e Camadas Bronze, Silver, Gold: arquitetura medalhão em Data Lakes/pipelines de dados. Delta Live Tables: automatização, confiabilidade, incrementalidade, monitoramento em tempo real para pipelines ETL, data warehouses/lakehouses, data quality assurance, ML/análise avançada, auditoria e rastreamento.
- Camadas medalha (Bronze/Silver/Gold): preservação de dados brutos (Bronze), limpeza e validação (Silver), refinamento e consumo (Gold); benefícios de escalabilidade, confiabilidade, flexibilidade e auditoria.
- Monitoramento e alertas: acompanhamento de status de jobs, métricas de desempenho, notificações automáticas, integração com ferramentas externas (Datadog, Prometheus, Azure Monitor).
- Estratégias de escalabilidade: auto-scaling de clusters, cluster pools, separação de workloads, particionamento de dados, Delta Lake otimizations, caching, otimizações de shuffle, multi-tenancy, clusters de streaming, ajustes de configurações Spark.
- Catálogo de dados e qualidade: organização centralizada de tabelas/esquemas, visão de descoberta/linhagem/metadados, carregamento com wildcard patterns, pipelines triggered vs contínuos, streaming com STREAM, restrições de qualidade com CONSTRAINT, visualização de grafo de DAG, lineage tracking (upstream/downstream), monitoramento integrado.

## Notas

- `00_def_agdd_14062025.md`
- `01_def_agdd_16062025.md`
- `02_def_agdd_17062025.md`
- `03_def_agdd_23062025.md`
- `04_def_agdd_24062025.md`
- `05_def_agdd_25062025.md`
- `06_def_agdd_26062025.md`
- `07_def_agdd_27062025.md`
- `08_def_agdd_02072025.md`
- `09_def_agdd_04072025.md`
- `10_def_agdd_08072025.md`
- `11_def_agdd_10072025.md`
- `12_def_agdd_01082025.md`
- `13_def_agdd_04082025.md`
- `14_def_agdd_05082025.md`
- `15_def_agdd_06082025.md`
- `16_def_agdd_07082025.md`
- `17_def_agdd_11082025.md`
- `18_def_agdd_12082025.md`
- `19_def_agdd_13082025.md`
- `20_def_agdd_14082025.md`
- `21_def_agdd_15082025.md`
- `22_def_agdd_19082025.md`
- `23_def_agdd_26082025.md`
- `24_def_agdd_27082025.md`
- `25_def_agdd_28082025.md`
- `26_def_agdd_29082025.md`
- `27_def_agdd_30082025.md`
- `28_def_agdd_31082025.md`
- `29_def_agdd_02092025.md`

Voltar para [Formação Engenheiro de Dados](../README.md).
