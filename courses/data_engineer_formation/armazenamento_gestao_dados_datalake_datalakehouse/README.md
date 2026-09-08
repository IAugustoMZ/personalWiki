# Armazenamento e Gestão de Dados com Datalake e Datalakehouse

12 notas sobre arquitetura de armazenamento de dados: diferenças entre Data Lake e Data Lakehouse, evolução dos conceitos, componentes e arquiteturas de referência, segurança/privacidade, ferramentas de mercado, planejamento de custos (on-premises, nuvem e análise comparativa), futuro tecnológico, metodologia de implementação ágil, design/implementação prática de Data Lakes locais com camadas de armazenamento e processamento distribuído, segurança operacional, performance, backup/recuperação e ferramentas de gerenciamento.

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

Voltar para [Formação Engenheiro de Dados](../README.md).
