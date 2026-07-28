# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Programação em Banco de Dados com Linguagem SQL

#### Sugestões de Melhorias na Query SQL

- **evitar o `CROSS JOIN`**: usar um `JOIN` mais apropriado para refletir a relação lógica entre as tabelas
  - redução de linhas processadas
- **eliminar subconsultas desnecessárias**: apenas aumentam a carga de processamento
  - subqueries somente quando necessário
  - CTEs podem ser uma alternativa de melhor performance
- **limitar as colunas desnecessárias**: apenas as consultas desejadas devem ser consultadas
- **otimizar a cláusula ORDER BY**: somente ordenações necessárias ou somente aquelas que impactam o resultado

- para analisar o desempenho da query, podemos nos guiar pelo custo e pelo número de linhas
  - leitura debaixo para cima
- **seq scan** $\to$ escaneamento sequencial
  - pode ser o gargalo se a tabela for muito grande
  - o ideal é que o seq scan seja feito numa tabela pequena nas primeiras etapas
- **hash** $\to$ construção de uma tabela na memória com as junções
  - a ideia é paralelizar operações
- **materialize** $\to$ uso do disco para armazenar dados intermediários
  - o ideal é manter operações na memória RAM (bem mais rápido)
- uso de `CROSS JOIN` causa a utilização de seq scan múltiplas vezes
- estratégias de melhoria da query
  - escrita da query
  - indexação
  - particionamento de tabelas
- operações foco na otimização: `JOINs`, `SORTs`
- para realizar o particionamento:

```sql
CREATE TABLE <name_table> (
    ...
) PARTITION BY (<col_part>)
```

- criando as partições:

```sql
CREATE TABLE <name_partition> PARTITION OF <name_table>
FOR VALUES FROM (<int_inc>) TO (<int_exc>)
```

- usar chave de particionamento na consulta

### Como usar Inteligência Artificial e Machine Learning com SQL?

- **análise preditiva em bancos de dados**: integração para predição com base em novos dados
- **processamento de linguagem natural**: análise de interpretação de textos armazenados em SQL
- **detecção de fraudes**: padrões suspeitos e anômalos em transações armazenadas em SQL
- **otimização de consultas SQL**: padrões de acesso e otimização automática de consultas
- **recomendação personalizada**: integrar sistemas de recomendção a bancos SQL
- **automação de manutenção**: automatizar limpeza e manutenção de dados em bases SQL
  - detecção e correção de erros
  - preenchimento de valores ausentes
  - identificação de duplicatas
- **visualização de dados e geração de insights**: análise automaizada, tendências, padrões e correlações

### O que é Processamento de Linguagem Natural?

- intersecção entre ciência da computação, inteligência artificial e linguística
  - algoritmos capazes de entender e interpretar a linguagem humana
  - executar tarefas relacionadas à linguagem
- objetivo: facilitar a comunicação homem-máquina
- redes neurais profundas e aprendizado de máquina
- LLMs (Large Language Models)
  - redes neurais profundas treinadas com quantidades massivas de dados
    - ampla variedade de padrões de linguagem
  - geração de texto
  - tradução de idiomas
  - sumarização
  - respostas a perguntas
  - análise de sentimentos
  - compreensão de texto
- capacidade de generalização: entendimento contextual e flexibilidade para diferentes tarefas
  - sem treinamento adiciona
  - pré-treinamento massico em dados diversificados e ampla gama de conhecimentos linguísticos e do mundo
- *Generative Pre-trained Transformer* $\to$ GPT