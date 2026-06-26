# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Cláusula `OVER` e Cláusula `PARITION BY`

- função de janela -> cálculo em conjunto de linhas da tabela, de alguma forma relacionadas à linha atual
  - ao contrário da agregação, as linhas não são agrupadas numa única linha de saída
  - nos bastidores, a função em janela acessa mais do que a linha atual

```sql
SELECT 
    id,
    valor,
    SUM(valor) OVER () AS total_geral
FROM vendas;
```

- função de janela sempre contém a cláusula `OVER`
  - distinção da função nominal ou de um agregado
  - determina como as linhas da consulta são divididas para processamento pela função da janela

```sql
SELECT 
    funcionario_id,
    salario,
    AVG(salario) OVER () AS media_salarial,
    ROW_NUMBER() OVER (ORDER BY salario DESC) AS ranking
FROM funcionarios;
```

- cláusula `PARTITION BY` divide as linhas em grupos ou partições
  - compartilham os mesmos valores da expressão `PARTIION BY`
  - para cada linha, a função da janela é calculada nas linhas que caem na mesma partição da linha atual

```sql
SELECT 
    departamento,
    funcionario,
    salario,
    SUM(salario) OVER (PARTITION BY departamento) AS total_departamento,
    AVG(salario) OVER (PARTITION BY departamento) AS media_departamento
FROM funcionarios;
```

- controlar a ordem que as linhas são processadas usando `ORDER BY`

```sql
SELECT 
    mes,
    receita,
    SUM(receita) OVER (ORDER BY mes) AS receita_acumulada,
    LAG(receita) OVER (ORDER BY mes) AS receita_mes_anterior
FROM receitas
ORDER BY mes;
```