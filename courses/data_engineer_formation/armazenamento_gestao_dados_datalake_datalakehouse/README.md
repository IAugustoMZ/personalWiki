# Armazenamento e Gestão de Dados com Datalake e Datalakehouse

17 notas sobre arquitetura de armazenamento de dados: diferenças entre Data Lake e Data Lakehouse, evolução dos conceitos, componentes e arquiteturas de referência, segurança/privacidade, ferramentas de mercado, planejamento de custos (on-premises, nuvem e análise comparativa), futuro tecnológico, metodologia de implementação ágil, design/implementação prática de Data Lakes locais com camadas de armazenamento e processamento distribuído, segurança operacional, performance, backup/recuperação, ferramentas de gerenciamento, design de solução com Terraform e automação, otimização/escalabilidade com gerenciamento de custos, governança com linhagem/observabilidade/qualidade, e enriquecimento de dados com documentação e metadados.

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

Voltar para [Formação Engenheiro de Dados](../README.md).
