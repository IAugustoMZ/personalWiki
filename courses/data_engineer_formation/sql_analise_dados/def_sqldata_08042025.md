# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Cláusula `OVER` e Cláusula `PARITION BY`

- crescimento das vendas diárias em relação ao dia anterior

```sql
SELECT
    data_venda,
    valor_venda,
    COALESCE(
        valor_venda - LAG(valor_venda) OVER (ORDER BY data_venda), 0
    ) AS crescimento
FROM vendas
```

- soma acumulada dia a dia

```sql
SELECT
    data_venda,
    SUM(venda_valor) OVER (
        PARTITION BY EXTRACT(MONTH FROM data_venda)
        ORDER BY data_venda
    ) AS soma_acumulada
FROM vendas
```

- no caso de valores acumulados, devemos particionar por uma granularidade maior
  - acumulado por dia -> particionar por mês
  
- ranking de vendas por funcionário considerando o valor total de vendas por e de cada funcionáio

```sql
SELECT *,
    DENSE_RANK() OVER (
        PARTITION BY funcionario ORDER BY valor_venda DESC
    ) AS rank_vendas
FROM
    (
        SELECT 
            data_venda,
            funcionario_id,
            SUM(valor_venda) AS valor_venda
        FROM vendas
        GROUP BY data_venda, funcionario_id
    ) AS subquery
ORDER BY funcionario_id, rank_vendas
```

### O que exatamente estamos procurando na Análise Exploratória de Dados?

- entender os dados e extrari insights
  - distribuição e tendência, padrões e outliers
    - histogramas, boxplots, density plots
  - correlações
  - tendências temporais
    - ciclos e sazonalidade
  - identificar e tratar dados ausentes
    - valores extremos e anomalias
  - segmentação de dados
    - estratificação
  - estatísticas descritivas
  - testes de hipóteses
  - visualizações de dados
    - gráficos de barras, linhas, mapas de calor, e gráficos de área
  - integração de conhecimento de domínio e contexto
  - qualidade e confiabilidade dos dados
    - errors e vieses
- abordagem flexível -> descobertas levam a novas perguntas e análises