<h1 align="center">Formação de Engenheiro de Dados</h1>

<p align="center">
  <strong>Uma trilha ampla para projetar, construir e governar plataformas de dados.</strong><br>
  Infraestrutura, armazenamento, transformação, SQL, analytics e desenvolvimento profissional.
</p>

<p align="center">
  <img src="https://cdn.simpleicons.org/terraform/844FBA" height="26" alt="Terraform"> &nbsp;
  <img src="https://cdn.simpleicons.org/amazonaws/FF9900" height="26" alt="AWS"> &nbsp;
  <img src="https://cdn.simpleicons.org/microsoftazure/0078D4" height="26" alt="Azure"> &nbsp;
  <img src="https://cdn.simpleicons.org/databricks/FF3621" height="26" alt="Databricks"> &nbsp;
  <img src="https://cdn.simpleicons.org/dbt/FB5A3E" height="26" alt="dbt"> &nbsp;
  <img src="https://cdn.simpleicons.org/apachekafka/231F20" height="26" alt="Apache Kafka">
</p>

## Visão geral

Esta é a principal formação técnica do wiki. Os módulos são independentes o suficiente para
consulta rápida, mas juntos formam uma visão de ponta a ponta: da infraestrutura e do
armazenamento à modelagem, transformação, processamento distribuído e governança.

## Módulos

| Módulo | Pergunta central | Acesso |
|---|---|---|
| **Infraestrutura como código** | Como provisionar ambientes de dados repetíveis? | [Terraform, AWS, Azure e Databricks](iac_terraform_aws_azure_databricks/README.md) |
| **Armazenamento e lakehouse** | Como organizar dados brutos, processados e confiáveis? | [Datalake e Datalakehouse](armazenamento_gestao_dados_datalake_datalakehouse/README.md) |
| **Modelagem e governança** | Como transformar dados em modelos úteis e controlados? | [Data warehouses](modeling_implementation_governance_data_warehouses/README.md) |
| **Integração e transformação** | Como extrair, carregar e transformar dados? | [Airbyte, dbt e SQL](data_engineering_airbyte_dbt_sql/README.md) |
| **Análise de dados** | Como responder perguntas de negócio com SQL? | [SQL para análise](sql_analise_dados/README.md) |
| **Processamento distribuído** | Como lidar com batch, streaming e mensagens? | [PySpark e Kafka](pyspark_kafka_processamento_batch_streaming/README.md) |
| **Desenvolvimento profissional** | Como sustentar a prática técnica e a carreira? | [Bônus da formação](personal_improvement_bonus/README.md) |

## Mapa de competências

```mermaid
flowchart LR
    I["Infraestrutura"] --> S["Storage e lakehouse"]
    S --> T["Ingestão e transformação"]
    T --> M["Modelagem e serving"]
    M --> G["Governança e qualidade"]
    G --> A["Analytics e produtos de dados"]
```

## Como navegar

1. Use a tabela acima para escolher o módulo mais próximo do seu objetivo.
2. Dentro de cada módulo, comece pelo README e siga as notas numeradas.
3. Abra os [artefatos visuais](../../artifacts/README.md) quando uma arquitetura precisar de contexto.
4. Relacione os conceitos às [questões de revisão](../../questions/README.md) e a exemplos executáveis.

Voltar para [Cursos](../README.md) ou para a [Personal Knowledge Wiki](../../README.md).
