# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Cláusula `OVER` e Cláusula `PARITION BY`

- query da média móvel

```sql
SELECT funcionario,
    ano,
    mes,
    unidades_vendidas,
    ROUND(
        AVG(unidades_vendidas) OVER (
            PARTITION BY funcionario ORDER BY ano
            CASE WHEN mes = 'Janeiro' THEN 1
            ...
            END
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ), 2
    ) AS media_movel
FROM vendas
```

- `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` - especificação da janela deslizante pegando 3 datas (1 antes, o presente e 1 após)
- funções de inteligência temporal

```sql
SELECT
    funcionario,
    ano,
    mes,
    unidades_vendidas,
    LEAD(unidades_vendidas) OVER (
        PARTITION BY funcionarios ORDER BY ano CASE
            WHEN mes = 'Janeiro' THEN 1
            ...
            END
    ) AS proxima_transcao
FROM vendas
```

- `LEAD` -> puxa o próximo valor de acordo com a janela
  - podemos substituir nulos com `COALESCE`
- `LAG` -> semelhante ao `LEAD`, porém buscando os valores prévios

- algumas consultas podem ser feitas com subqueries
  - cuidados com problemas de performance
  - funções window geralmente têm desempenho melhor

- funcionarios juntamente com o valor máximo de unidades vendidas no ano de cada um, comparando com a média de vendas do ano

```sql
SELECT
    v.funcionario,
    v.ano,
    v.unidades_vendidas AS maior_venda_ano,
    (
        SELECT ROUND(
            AVG(unidades_vendidas), 2
        )
        FROM vendas
    ) AS media_vendas_ano
FROM vendas v
WHERE
    v.unidades_vendidas = (
            SELECT (
                MAX(unidades_vendidas)
            FROM vendas
            WHERE funcionario = v.funcionario AND
                ano = v.ano
        )
    )
ORDER BY v.funcionario, v.ano
```

- query dentro dos parênteses -> query interna
- se a uery interna referencia colunas da tabela da query externa -> subqueries corretas

- número de unidades vendidas cada funcionário e o percentual em relação ao total geral (todos os anos) de unidades vendidas de cada funcionário

```sql
SELECT
    v.funcionario,
    ano,
    mes,
    unidades_vendidas,
    ROUND((unidades_vendidas / total_vendas) * 100, 2) AS percentual_do_total
FROM vendas AS v,
    (
        SELECT
            funcionarios,
            SUM(unidades_vendidas) AS total_vendas
        FROM vendas
        GROUP BY funcionario
    ) AS vendas_totais
WHERE
    v.funcionario = vendas_totais.funcionario
ORDER BY v.funcionario, ano,
    CASE
        WHEN mes = 'Janeiro' THEN 1
        ...
    END;
``` 