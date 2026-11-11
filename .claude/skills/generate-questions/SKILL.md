---
name: generate-questions
description: Generate review questions from a folder of wiki notes, present them in chat for approval by question number, regenerate the rejected ones, and register the approved ones in the timesheet question bank (ADR-009). Use when the user asks to generate, create or validate study questions from a folder.
---

# generate-questions

Generates multiple-choice review questions from a folder of notes. Nothing is saved to the
timesheet until the user approves it by number in chat.

## Inputs

- `folder`: a path under `courses/` (or any folder of Markdown notes).
- `n` (optional, default `10`): questions **per flavor**. There are four flavors, so the round
  has `4n` questions.

## Flavors

| Flavor | Grounding | Intent |
|---|---|---|
| `easy` | Only what the notes state | Direct recall, no outside knowledge |
| `medium` | About 80% notes, 20% general practice | Systemic understanding |
| `hard` | About 50% notes, 50% reasoning and experience | Diagnose, compare or predict |
| `expert` | Notes give the base concept only | Strategy, roadmap, critical judgment |

## Kinds (required in every flavor)

Every flavor must contain at least `max(1, ceil(0.2 * n))` questions of kind `code` and at least
`max(1, ceil(0.2 * n))` of kind `equation`. The rest are kind `concept`.

**Language folders** (anything under `languages/`) add a fourth kind, `grammar`: every flavor must
also contain at least `max(1, ceil(0.2 * n))` grammar questions. Grammar progress is tracked
separately from vocabulary, so do not let vocabulary questions fill that quota.

- **`code`**: a fenced code block with one or more blanks marked `____`, or a function, measure,
  or keyword name to recall. The options are the candidate fills. Use the language of the notes
  (DAX, M, Python, SQL). In language folders, `code` means a translation or fill-in-the-blank snippet.
- **`equation`**: the question states a formula in LaTeX. Inline math uses `$...$`. Display math
  uses `$$` on its own lines.
- **`grammar`** (language folders): tests a rule, not a word. Quote the target-language sentence or
  pattern in the question and ask about conjugation, agreement, particles, articles, word order,
  tense or sentence building (fill the correct form, spot the error, choose the right structure,
  explain why a form is used). Distractors must be plausible wrong forms. The explanation states
  the rule and gives one more example. Every note under `languages/` has a "Gramática em exemplos"
  section: draw these questions from it and from the grammar points implied by the unit theme.
  Each grammar question must name its point in the explanation (for example "present tense of
  *ser*") so progress can be tracked per point.

## Content rules (non-negotiable)

- Questions, options and explanations must be understandable without the notes. **Never** refer
  to note numbers, file names, lab or lesson numbers, "the sample", "the example", or "the notes".
  Every question carries the data it needs.
- Exactly four options, distinct, exactly one correct.
- Every question has an `explanation` that teaches the concept. It is shown to the learner after
  a wrong answer, so it must not refer to the notes either.
- Write in English, to match `questions/bi_powerbi.json`.
- Markdown is allowed in question text, options and explanations. Raw HTML is not rendered.
- Code fences and math delimiters must be balanced.

## Workflow

1. **Read the folder.** Read every Markdown note. Identify the concepts, formulas and code.
2. **Propose the topic.** Map the folder to a timesheet topic (`subsubcategory_id`). Show the
   proposed location and whether it exists. Wait for the user to confirm or change it.
   Create nothing until confirmed.
3. **Generate the round.** Number the questions `1..4n`, grouped by flavor. Give each question
   its flavor, kind, options, and an answer key line for the user's check. Do not show note numbers.
4. **Validate the round.** Run `python questions/validate_questions.py <round.json> --per-flavor <n>`
   on a draft JSON of the round. For language folders add `--grammar`. Fix any failure before presenting.
5. **Present the round in chat.** Ask the user to reply with the numbers to approve, for example
   `1 3 6 9 11 16`.
6. **Regenerate the rest.** Replace every unapproved number in place, keeping its number and
   flavor, and present only the replaced questions. Repeat from step 4.
7. **Register approved questions.** Call `POST /learning/questions/import` with the approved items
   (requires `QUESTION_IMPORT_ENABLED=true`). Items already in the topic are skipped and reported.
8. **Save the audit record.** Write the approved items to `questions/<folder-slug>_roundN.json`,
   with `approved_by`, `approved_on`, `topic` and each item's `number`, `kind` (`concept`, `code`, `equation` or `grammar`), `difficulty`,
   `question_text`, `options`, `correct_option`, `explanation`. Commit only when the user asks.

## Output format for each question in chat

```
**12.** [hard · concept] Question text, with $math$ or a ```code``` block when needed.
A) ...  B) ...  C) ...  D) ...
*Key: C · explanation shown on a miss: ...*
```

## Validation

`questions/validate_questions.py` checks: schema, four distinct options, one correct answer,
explanation present, flavor counts, minimum code and equation questions per flavor, reference
guard, balanced Markdown and LaTeX, and (with `--grammar`) the minimum grammar questions per flavor. It exits non-zero when any check fails.
