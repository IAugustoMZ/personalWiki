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
| [`chinese_duolingo_levels_01_09_round1.json`](chinese_duolingo_levels_01_09_round1.json) | Chinês: Duolingo, níveis 1–9 (40 perguntas, 10 por nível) | [Notas de Chinês](../languages/chinese/00_lan_chn_10082026.md) |

## Validação

Antes de registrar uma nova rodada, valide-a com o script de regras:

```bash
python questions/validate_questions.py questions/bi_powerbi_round3.json --per-flavor 10
```

O script confere quantidade por nível, alternativas, referências a material não visível ao aluno, blocos de código, equações LaTeX e marcadores de Markdown.

## Estratégia de uso

1. Leia uma nota ou módulo.
2. Feche o material e tente responder sem consultar.
3. Registre a dúvida e volte ao conceito correspondente.
4. Repita em intervalos diferentes para consolidar a memória.

Voltar para a [Personal Knowledge Wiki](../README.md).
