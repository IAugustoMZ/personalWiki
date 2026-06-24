# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### O que exatamente estamos procurando na Análise Exploratória de Dados?

- query mostrando diversas métricas por centro de custo

```sql
SELECT
    centro_custo,
    COUNT(*) AS contagem_lancamentos,
    SUM(valor) AS total_valor_lancamentos,
    ROUND(AVG(valor), 2) AS media_lancamentos,
    MAX(valor) AS maior_valor,
    MIN(valor) AS menor_valor,
    SUM(
        CASE
            WHEN moeda = 'USD' THEN valor
            ELSE 0
        END
    ) AS soma_usd,
    ROUND(
        AVG(
            CASE
                WHEN taxa_conversao IS NOT NULL THEN taxa_conversao
                ELSE 0
            END
        ), 2
    ) AS media_taxa_conversao,
    PERCENTILE_COUNT(0.5) WITHIN GROUP(ORDER BY valor) AS mediana_valores
FROM lancamentos_contabeis
GROUP BY centro_custo
ORDER BY total_valores_lancamentos DESC
```

#### O que é Percentil?

- medida estatística que indica o valor abaixo do qual uma determinada porcentagem dos dados num conjunto, cai
  - $P_{20} \to$ 20% dos dados estão abaixo
- definição formal: o $p$-ésimo percentil $P_p$ é o valor $x$ tal que:

$$P_p = \frac{p}{100} \cdot (N + 1)\text{-ésimo valor ordenado}$$

- usados para estudar a distribuição dos dados
  - identificação de valores atípicos
  - valores esperados
- valores comuns: $P_{25}$, $P_{50}$, $P_{75}$ $\to$ primeiro quartil, mediana e terceiro quartil

#### O que é Distribuição de Dados?

- maneira com a qual um conjunto de dados estão espalhados ou organizados
- visualização de dados ajuda a entender a distribuição
  - formas variadas
  - medidas de tendência central (média, mediana e moda)
    - média: $\mu = \dfrac{1}{N}\displaystyle\sum_{i=1}^{N} x_i$
  - medidas de dispersão $\to$ espalhamento dos dados
    - desvio padrão: $\sigma = \sqrt{\dfrac{1}{N}\displaystyle\sum_{i=1}^{N}(x_i - \mu)^2}$
    - variância: $\sigma^2 = \dfrac{1}{N}\displaystyle\sum_{i=1}^{N}(x_i - \mu)^2$
    - amplitude: $A = x_{\max} - x_{\min}$
    - quartis e percentis
  - assimetria e curtose $\to$ forma da distribuição de dados
    - assimetria: $\gamma_1 = \dfrac{1}{N}\displaystyle\sum_{i=1}^{N}\left(\dfrac{x_i - \mu}{\sigma}\right)^3$
    - curtose: $\gamma_2 = \dfrac{1}{N}\displaystyle\sum_{i=1}^{N}\left(\dfrac{x_i - \mu}{\sigma}\right)^4 - 3$
  - valores atípicos $\to$ valores que se desviam da distribuição majoritária
- influencia escolha de métodos estatísticos
- podem ser determinadas por testes de hipóteses