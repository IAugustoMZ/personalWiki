# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Cláusula `OVER` e Cláusula `PARITION BY`

- unidades vendidas por ano para cada funcionário, total em unidades vendidas em cada ano e proporcional de cada funcionário em relação ao total do -> desafio do relatório

```sql
SELECT
    YEAR(data_venda)                                        AS ano,
    funcionario,
    SUM(unidades_vendidas)                                  AS unid_funcionario,
    SUM(SUM(unidades_vendidas)) OVER (PARTITION BY YEAR(data_venda))
                                                            AS total_ano,
    ROUND(
        SUM(unidades_vendidas) * 100.0
        / SUM(SUM(unidades_vendidas)) OVER (PARTITION BY YEAR(data_venda)),
        2
    )                                                       AS pct_funcionario
FROM vendas
GROUP BY
    YEAR(data_venda),
    funcionario
ORDER BY
    ano,
    unid_funcionario DESC;
```

- unidades vendidas por ano, mês e funcionário, total de unidades vendidas no ano e proporcional de cada funcionário em relação ao total do ano

```sql
SELECT
    ano, 
    mes,
    funcionario,
    unidades_vendidas
    SUM(
        unidades_vendidas
    ) OVER (PARTITION BY ano) AS unidades_vendidas_ano,
    ROUND(
        unidades_vendidas
     / SUM(unidades_vendidas) OVER (PARTITION BY ano) * 100, 2) AS proporcional
FROM vebdas
ORDER BY ano, funcionario
```

- os dados continuam vindo como linhas mensais (função window só faz agregação por linha)
  - não resolve o problema pois queremos agregar os meses de cada ano

- opção 2: função window + `GROUP BY`

```sql
SELECT
    ano, 
    funcionario,
    unidades_vendidas,
    SUM(unidades_vendidas) OVER (PARTITION BY ano) AS unidades_vendidas_ano,
    ROUND(
        unidades_vendidas / SUM(unidades_vendidas) OVER (PARTITION BY ano) * 100, 2 
    ) AS proporcional_func_ano
FROM vendas
GROUP BY ano, funcionario, unidades_vendidas
ORDER BY ano, funcionario
```

- não podemos tirar `unidades_vendidas` do `GROUP BY` pois o window function não é um agrupamento por colunas
- nesse caso, o `GROUP BY` não modificou a consulta e trouxe uma operação a mais -> performance

- opção 3 - CTE \& VIEWs temporárias

```sql
WITH vendas_agregadas AS (
    SELECT
        ano,
        funcionario,
        SUM(unidades_vendidas) AS total_unidades_vendidas
    FROM vendas
    GROUP BY ano, funcionario
),
total_ano AS (
    SELECT
        ano,
        SUM(total_unidades_vendidas) AS total_unidades_ano
    FROM vendas_agregadas
    GROUP BY ano
)
SELECT
    v.ano,
    v.funcionarios,
    v.total_unidades_vendidas,
    t.total_unidades_ano,
    ROUND(
        v.total_unidades_vendidas / t.total_unidades_ano * 100, 2
    ) AS proporcional_func_ano
FROM vendas_agregadas v
    JOIN total_ano t
        ON v.ano = t.ano
ORDER BY v.ano, v.funcionario
```

- a consulta está correta e entra o resultado esperado
  - mas é computationalmente custosa

- opção 4: função window + `GROUP BY`

```sql
SELECT
    ano,
    funcionario,
    SUM(unidades_vendidas) AS total_unidades_venda,
    SUM(SUM(unidades_vendidas)) OVER (PARTITION BY ano) AS total_vendas_ano,
    ROUND((SUM(unidades_vendidas) / SUM(SUM(unidades_vendidas)) OVER (PARTITION BY ano)) * 100, 2) AS proporcional_func_ano
FROM vendas
GROUP BY ano, funcionario
ORDER BY ano, funcionario
```

- o uso da `SUM` sem o `PARTITION` permite a agregação por coluna

### Funções Window e SubQueries - Parte 2

- não é bom premissar a ordenação dos dados
- podemos usar a função `ROW_NUMBER()` paar numerar as linhas e unir com indexação de texto para ordenação

```sql
SELECT
    functionario,
    ano,
    mes,
    unidades_vendidas,
    ROW_NUMBER() OVER (
            PARTITION BY funcionario,
            ORDER BY ano
            CASE
                WHEN mes = 'Janeiro' THEN 1
                WHEN mes = 'Fevereiro' THEN 2
                ...
            END
        ) AS numero_transacoes
FROM vendas
WHERE funcionario = '...'
```

- sempre que precisamos ordenar tipo texto, ele será ordenado de forma alfabética
  - se quisermos ordenar de forma diferente, devemos criar uma indexação com `CASE`
- para ajudar na ordenação podemos usar a função `RANK()`

```sql
SELECT
    funcionario,
    ano,
    mes,
    unidades_vendidas,
    RANK() OVER (
        PARTITION BY ano
        ORDER BY unidades_vendidas DESC
    ) AS rank_vendas
FROM vendas
```

- podemos também colocar a função janela dentro de uma subquery para obter informações de uma linha específica do ranking

```sql
SELECT *
FROM (
    SELECT
        funcionario,
        ano,
        mes,
        unidades_vendidas,
        RANK() OVER (
            PARTITION BY ano
            ORDER BY unidades_vendidas DESC
        ) as rank_vendas
    FROM vendas
) AS subquery
WHERE rank_vendas = 1
```

- subqueries podem ser aninhadas
- se usamos a função `DENSE_RANK()`, linhas com valores empatados recebem o mesmo índice
  - continha a sequência depois do empate
  - se fosse a `RANK()`, teria o empate, e o próximo número seria pulado
    - ex: dois valores empatados em 2, o 3 seria pulado com `RANK()`