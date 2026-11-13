<h1 align="center">Questões de Revisão</h1>

<p align="center">
  <strong>Recuperação ativa para transformar leitura em domínio.</strong><br>
  Bancos de perguntas relacionados às trilhas de estudo do wiki.
</p>

<p align="center">
  <img src="https://cdn.simpleicons.org/json/000000" height="28" alt="JSON"> &nbsp;
  <img src="https://cdn.simpleicons.org/microsoftpowerbi/F2C811" height="28" alt="Power BI"> &nbsp;
  <img src="https://cdn.simpleicons.org/python/3776AB" height="28" alt="Python">
</p>

## Banco disponível

| Arquivo | Tema | Relacionado |
|---|---|---|
| [`bi_powerbi.json`](bi_powerbi.json) | Business Intelligence e Power BI (179 perguntas) | [Curso de Power BI](../courses/microsoft_power_bi_for_business_intelligence_and_data_science/README.md) |
| [`bi_powerbi_round2.json`](bi_powerbi_round2.json) | Power BI, rodada 2 (20 perguntas, 5 por nível) | [Curso de Power BI](../courses/microsoft_power_bi_for_business_intelligence_and_data_science/README.md) |
| [`bi_powerbi_round3.json`](bi_powerbi_round3.json) | Power BI, rodada 3 (40 perguntas, 10 por nível) | [Curso de Power BI](../courses/microsoft_power_bi_for_business_intelligence_and_data_science/README.md) |
| [`data_engineering_fundamentals_round1.json`](data_engineering_fundamentals_round1.json) | Data Engineering Fundamentals, round 1 (200 questions, 50 per difficulty) | [Data Engineering Fundamentals](../courses/data_engineering_fundamentals/README.md) |
| [`chinese_duolingo_levels_01_09_round1.json`](chinese_duolingo_levels_01_09_round1.json) | Chinês: Duolingo, níveis 1–9 (40 perguntas, 10 por nível) | [Notas de Chinês](../languages/chinese/00_lan_chn_10082026.md) |
| [`spanish_duolingo_levels_01_41_round1.json`](spanish_duolingo_levels_01_41_round1.json) | Espanhol: Duolingo, níveis 1–41 (200 perguntas, 50 por dificuldade) | [Notas de Espanhol](../languages/spanish/00_lan_spn_10082026.md) |
| [`english_duolingo_levels_01_45_round1.json`](english_duolingo_levels_01_45_round1.json) | Inglês: Duolingo, níveis 1–45 (200 perguntas, 50 por dificuldade) | [Notas de Inglês](../languages/english/00_lan_eng_10112026.md) |
| [`french_duolingo_levels_01_24_round1.json`](french_duolingo_levels_01_24_round1.json) | Francês: Duolingo, níveis 1–24 (200 perguntas, 50 por dificuldade) | [Notas de Francês](../languages/french/00_lan_fra_10112026.md) |
| [`italian_duolingo_levels_01_21_round1.json`](italian_duolingo_levels_01_21_round1.json) | Italiano: Duolingo, níveis 1–21 (200 perguntas, 50 por dificuldade) | [Notas de Italiano](../languages/italian/00_lan_ita_10112026.md) |
| [`german_duolingo_levels_01_23_round1.json`](german_duolingo_levels_01_23_round1.json) | Alemão: Duolingo, níveis 1–23 (200 perguntas, 50 por dificuldade) | [Notas de Alemão](../languages/german/00_lan_deu_10112026.md) |
| [`chinese_duolingo_levels_01_09_round2.json`](chinese_duolingo_levels_01_09_round2.json) | Chinês: Duolingo, níveis 1–9, rodada 2 (200 perguntas, 50 por dificuldade) | [Notas de Chinês](../languages/chinese/00_lan_chn_10082026.md) |
| [`japanese_duolingo_levels_01_10_round1.json`](japanese_duolingo_levels_01_10_round1.json) | Japonês: Duolingo, níveis 1–10 (200 perguntas, 50 por dificuldade) | [Notas de Japonês](../languages/japanese/00_lan_jpn_10082026.md) |

## Validação

Antes de registrar uma nova rodada, valide-a com o script de regras:

```bash
python questions/validate_questions.py questions/bi_powerbi_round3.json --per-flavor 10
```

Para rodadas de idiomas (pasta `languages/`), acrescente `--grammar`: cada nível passa a exigir perguntas do tipo `grammar`, para acompanhar a gramática separadamente do vocabulário.

```bash
python questions/validate_questions.py questions/<rodada_de_idioma>.json --per-flavor 10 --grammar
```

`--per-flavor` aceita um número (o mesmo para os quatro níveis) ou quatro contagens na ordem `easy,medium,hard,expert`. Use `50,50,0,0` ou `0,0,50,50` para validar metade de uma rodada de 200 perguntas, e `50` para a rodada completa:

```bash
python questions/validate_questions.py questions/spanish_duolingo_levels_01_41_round1.json --per-flavor 50 --grammar
```

O script confere quantidade por nível, alternativas, referências a material não visível ao aluno, blocos de código, equações LaTeX e marcadores de Markdown.

## Estratégia de uso

1. Leia uma nota ou módulo.
2. Feche o material e tente responder sem consultar.
3. Registre a dúvida e volte ao conceito correspondente.
4. Repita em intervalos diferentes para consolidar a memória.

Voltar para a [Personal Knowledge Wiki](../README.md).
