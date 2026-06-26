# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Conceito de `UNION` e `UNION ALL`

- operadores em SQL usados para combinar resultados de duas ou mais consultas num único conjunto de resultados
  - `UNION` -> combina e remove duplicatas para criar um conjunto de dados único
    - colunas devem ser as mesmas
  - `UNION ALL` -> inclui as linhas duplicadas
    - mais rápido que `UNION`, pois não precisa verificar a unicidade das linhas

### Boas Práticas ao Trabalhar com Junções

- `JOINs` podem levar a problemas de desempenho
- **ser específico na seleção de colunas**
  - evitar o `SELECT *` -> reduzir carga do banco de dados
- **use aliases para tabelas** -> mais legibilidade, evitar ambiguidades
- **especificar o tipo de junção** -> resultados esparsos
- **`JOIN`s em colunas indexadas** -> acelerar o desempenho da consulta
- **evitar o `CROSS JOIN`** -> número muito grande de linhas
- **condições de junções claras** -> precisão
- **cuidado com self JOINs** -> usar aliases para diferenciar cópias da tabela
- **testar num ambiente seguro** -> ambiente de desenvolvimento
- **monitorar desempenho** -> otimização de consultas
- **entender modelagem** -> esquema, relacionamento e chaves estrangeiras
- **evitar junções desnecessárias** -> sobrecarga sem valor