# Formação Engenheiro de Dados

## SQL para Análise de Dados e Data Science

### Tipos de Dados - Qualitativos e Quantitativos

- entender e categorizar as informações coletadas
- **quantitativos**: quantidades, podem ser mensurados em escala numérica
  - *discretos*: apenas valores inteiros, contagens
  - *contínuos*: medidas, podem assumir qualquer valor
- **qualitativos**: características que não podem ser medidas numericamente
  - *nominais*: sem ordem implícita
  - *ordinais*: ordem ou graduação específica, porém sem distâncias uniformes ou conhecidas entre categorias

### O que é Categorização?

- transformar dados numéricos contínuos ou discretos em categorias ou grupos discretos
  - binning ou bucketing
  - simplificar a análise ou visualização distribuições numéricas

1. **simplificação de análise**: grande variedade de dados numéricos
2. **visualização**: pode ser mais intuitivo para categorias
3. **tratamento de outliers**: agrupar valores extremos em categorias mais amplas
4. **preparação para modelos específicos**

- **definição de intervalos** - limites de definição das categorias
  - igual tamanho
  - percentis
  - conhecimento específico do domínio
- **transformação**
- **rotulação**: mais descritivos da categoria

### O que é Codificação (Encoding)?

- converter dados categóricos ou textuais em um formato numérico
  - demanda de algoritmos
- **one-hot-encoding** -> cada categoria única de uma variável é convertida em uma nova coluna binária (0, 1)
  - cada categoria recebe um valor inteiro
  - pode ser problemática em variáveis ordinais
- **frequency ou count encoding** -> usa a frequência para codificar
  - problemático se as frequências forem muito semelhantes entre categorias
- **target encoding** -> agregação do valor-alvo para essa categoria (média, mediana, ...)
  - cuidado com vazamento de dados
- **binary encoding** -> rótulos codificados binariamente
- **embedding-encoding** -> vetores densos num espaço n-dimensional, aprendidos durante o treinamento de redes neurais

### O que é Binarização?

- converter dados numéricos ou categóricos em formato binário, 0 ou 1
  - simplificação, preparação para algoritmos
  - extração de características relevantes
  - processamento de imagens
  - identificação e destacamento de relações não lineares
  - engenharia de atributos

#### Instrução `CASE`

- transformação dos dados em tempo de execução com base numa condicional

```sql
SELECT
    CASE
        WHEN <condition_1> THEN <value_when_condition_1_true>
        ...
    END AS <created_col_alias>
FROM ...
```

- se não quisermos modificar a tabela original -> criamos uma nova tabela com resultado do `SELECT`

```sql
CREATE TABLE <table_name> AS
    SELECT ...
```