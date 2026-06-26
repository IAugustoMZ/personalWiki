# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Cláusula `OVER` e Cláusula `PARITION BY`

- `NTILE(n)` -> divide a coluna particionada em n grupos (parecido com uma clusterização)

```sql
SELECT
    funcionario,
    ano,
    mes,
    unidades_vendidas,
    NTILE(2) OVER (PARTITION BY funcionario, ano ORDER BY unidades_vendidas DESC) AS grupo_vendas
FROM vendas
```

- cláusula `PARTITION BY` não é obrigatória
  - na ausência, a função window vai percorrer todos os dados
- função window também pode ser usada para calcular médias móveis
  - média acumulada até o período

```sql
SELECT
    funcionario,
    ano,
    mes,
    unidades_vendidas,
    ROUND(AVG(unidades_vendidas) OVER (
        PARTITION BY funcionario 
        ORDER BY ano
        CASE
            WHEN mes = 'Janeiro' THEN 1
            ...
        END), 2
    ) AS media_acumulada_ate_ponto_atual
FROM vendas
```