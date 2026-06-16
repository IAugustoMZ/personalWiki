# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Como funciona o `ROLLUP`?

- extensão da cláusulas `GROUP BY`:
  - usado em análises segregadas e multidimensionais
  - sumários e subtotais
- **agregação regular** -> resultados agregados pelas colunas específicas na cláusula `GROUP BY`
- **agregação hierárquica** -> níveis adicionais de agregação hierárquica
  - remoção sucessiva das colunas da direita para a esquerda
  - recalcula as agregações para cada nível
- **geração de subtotais** -> cada nível de agregação resulta num conjunto de subtotais
- **resultados** -> não apenas as agregações nominais (para cada combinação das colunas agrupamento)
  - subtotais
  - total geral
- `ROLLUP` permite o uso de múltiplas colunas para agregação
  ```sql
  SELECT
      ano,
      mes,
      SUM(valor_venda) AS total_vendas
  FROM vendas
  GROUP BY ROLLUP (ano, mes);
  -- gera: subtotal por (ano, mes), subtotal por (ano) e o total geral
  ```

### Como funciona o `CUBE`?

- facilita análises multidimensionais avançadas, com múltiplas combinações de subtotais e totais gerais
- **agregação multidimensional**: gera todas as combinações possíveis de subtotais para as colunas especificadas
  - agregações para cada combinação de colunas
  - agregações individuais
  - total geral
- **combinação de subtotais**
  - para A, B e C -> subtotais para
    - A, B, C, A + B, A + C, B + C, A + B + C, total geral
- **análise compreensiva dos dados**: diferentes dimensões interagem entre se para impactar resultados
  ```sql
  SELECT
      regiao,
      produto,
      SUM(valor_venda) AS total_vendas
  FROM vendas
  GROUP BY CUBE (regiao, produto);
  -- gera: subtotal por (regiao, produto), por (regiao), por (produto) e o total geral
  ```