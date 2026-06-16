# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

- window functions aplicam função de agregação na direção das linhas
  - `PARTITION BY` -> coluna que determina a partição
- **window function**
    - Aggregation
      - `AVG()`: calcula a média dos valores de uma coluna dentro da partição definida pela window function.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            AVG(salario) OVER (PARTITION BY departamento) AS media_departamento
        FROM funcionarios;
        ```
      - `MAX()`: retorna o maior valor de uma coluna dentro da partição.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            MAX(salario) OVER (PARTITION BY departamento) AS maior_salario_departamento
        FROM funcionarios;
        ```
      - `MIN()`: retorna o menor valor de uma coluna dentro da partição.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            MIN(salario) OVER (PARTITION BY departamento) AS menor_salario_departamento
        FROM funcionarios;
        ```
      - `SUM()`: soma os valores de uma coluna dentro da partição.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            SUM(salario) OVER (PARTITION BY departamento) AS total_departamento
        FROM funcionarios;
        ```
      - `COUNT()`: conta o número de linhas dentro da partição.
        ```sql
        SELECT
            funcionario,
            departamento,
            COUNT(*) OVER (PARTITION BY departamento) AS qtd_funcionarios_departamento
        FROM funcionarios;
        ```
    - Ranking
      - `ROW_NUMBER()`: atribui um número sequencial único e crescente para cada linha dentro da partição, sem repetir valores mesmo em caso de empate.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            ROW_NUMBER() OVER (PARTITION BY departamento ORDER BY salario DESC) AS posicao
        FROM funcionarios;
        ```
      - `RANK()`: atribui um ranking às linhas dentro da partição, repetindo a posição em caso de empate e deixando "buracos" na sequência seguinte.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) AS ranking
        FROM funcionarios;
        ```
      - `DENSE_RANK()`: igual ao `RANK()`, mas não deixa "buracos" na sequência quando há empate.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            DENSE_RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) AS ranking_denso
        FROM funcionarios;
        ```
      - `PERCENT_RANK()`: calcula o percentual relativo da posição da linha dentro da partição (varia de 0 a 1).
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            PERCENT_RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) AS percentual_ranking
        FROM funcionarios;
        ```
      - `NTILE()`: divide as linhas da partição em N grupos (baldes) de tamanho aproximadamente igual, retornando o número do grupo.
        ```sql
        SELECT
            funcionario,
            departamento,
            salario,
            NTILE(4) OVER (PARTITION BY departamento ORDER BY salario DESC) AS quartil
        FROM funcionarios;
        ```
    - Value
      - `LAG()`: retorna o valor de uma coluna da linha anterior dentro da partição.
        ```sql
        SELECT
            funcionario,
            data_venda,
            valor_venda,
            LAG(valor_venda) OVER (PARTITION BY funcionario ORDER BY data_venda) AS venda_anterior
        FROM vendas;
        ```
      - `LEAD()`: retorna o valor de uma coluna da próxima linha dentro da partição.
        ```sql
        SELECT
            funcionario,
            data_venda,
            valor_venda,
            LEAD(valor_venda) OVER (PARTITION BY funcionario ORDER BY data_venda) AS proxima_venda
        FROM vendas;
        ```
      - `FIRST_VALUE()`: retorna o primeiro valor de uma coluna dentro da partição, considerando a ordenação definida.
        ```sql
        SELECT
            funcionario,
            data_venda,
            valor_venda,
            FIRST_VALUE(valor_venda) OVER (PARTITION BY funcionario ORDER BY data_venda) AS primeira_venda
        FROM vendas;
        ```
      - `LAST_VALUE()`: retorna o último valor de uma coluna dentro da partição, considerando a ordenação definida (geralmente precisa ajustar o frame com `RANGE BETWEEN ... AND UNBOUNDED FOLLOWING` para funcionar como esperado).
        ```sql
        SELECT
            funcionario,
            data_venda,
            valor_venda,
            LAST_VALUE(valor_venda) OVER (
                PARTITION BY funcionario
                ORDER BY data_venda
                RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
            ) AS ultima_venda
        FROM vendas;
        ```
      - `NTH_VALUE()`: retorna o valor da N-ésima linha dentro da partição, considerando a ordenação definida.
        ```sql
        SELECT
            funcionario,
            data_venda,
            valor_venda,
            NTH_VALUE(valor_venda, 2) OVER (
                PARTITION BY funcionario
                ORDER BY data_venda
                RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
            ) AS segunda_venda
        FROM vendas;
        ```