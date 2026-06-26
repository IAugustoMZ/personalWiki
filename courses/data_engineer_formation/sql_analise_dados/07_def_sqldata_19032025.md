# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### `GROUPING`

- usada para determinar se uma coluna ou expressão em consulta está sendo agrupada ou se está em uma linha de subtotal ou total
- retorna `0` quando a coluna está sendo agrupada normalmente e `1` quando a linha é um subtotal/total gerado por `ROLLUP`, `CUBE` ou `GROUPING SETS`
  ```sql
  SELECT
      departamento,
      cargo,
      SUM(salario) AS total_salario,
      GROUPING(departamento) AS eh_total_departamento,
      GROUPING(cargo) AS eh_total_cargo
  FROM funcionarios
  GROUP BY ROLLUP (departamento, cargo);
  ```

### `STRING_AGG`

- concatena strings numa lista separada por um separador
- função específica do PostgreSQL (equivalente ao `GROUP_CONCAT` do MySQL e ao `LISTAGG` do Oracle/SQL Server)
  ```sql
  SELECT
      departamento,
      STRING_AGG(funcionario, ', ') AS funcionarios
  FROM funcionarios
  GROUP BY departamento;
  ```