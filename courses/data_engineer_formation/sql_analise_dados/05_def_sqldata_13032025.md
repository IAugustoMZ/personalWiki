# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Boas Práticas ao Trabalhar com Junções

- é possível fazer um `JOIN` com a cláusula `WHERE`
- para funções de agregação, colunas que não são agregadas, devem aparecer no `GROUP BY`
- se eu for usar o `COALESCE`, devo tomar cuidado para fazer o `CAST` da coluna para `VARCHAR`
  - podemos usar uma expressão `CASE`
  - cuidado com o `CAST` para texto, pois pode prejudicar a ordenação
    - podemos criar um "índice" para ordenação

```sql
ORDER BY
    CASE WHEN AVG(valor) IS NULL THEN 1
    ELSE 0
END
media DESC;
```
