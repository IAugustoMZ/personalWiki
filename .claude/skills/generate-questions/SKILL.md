---
name: generate-questions
description: Select a terminal wiki folder automatically, confirm its timesheet category, generate review questions, and register approved questions in the timesheet question bank (ADR-009). Use when the user asks to generate, create or validate study questions; no folder argument is needed.
---

# generate-questions

Generates multiple-choice review questions from a folder of notes. Nothing is saved to the
timesheet until the user approves it by number in chat.

## Inputs

- `n` (optional, default `10`): questions **per flavor**. There are four flavors, so the round
  has `4n` questions.

No folder path is required. Discover candidates under `courses/`, `certifications/`, `books/`
and `languages/` relative to the wiki repository root. A candidate must contain at least one
Markdown study note (`.md`, excluding `README.md`) directly inside it and **no child
directories**, including hidden directories. Do not treat a parent containing nested notes
as terminal, or follow directory symlinks outside the wiki. Exclude generated content,
question banks and tooling directories.

Select one eligible folder, favoring new material or topics with fewer existing review rounds.
Report its relative path and note count when proposing the category. Do not ask the user to
supply a path. If no folder qualifies, report that and stop. If the user requests another
folder, select another eligible candidate; validate any user-suggested folder by the same rules.

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

1. **Select and read a terminal folder.** Apply the selection rules above, then read every
   Markdown note directly in the selected folder. Identify the concepts, formulas and code.
2. **Propose the topic.** Map the folder to a timesheet topic (`subsubcategory_id`). Show the
   full category → subcategory → topic location, topic ID and whether it currently exists,
   checking the timesheet service rather than assuming an older audit record is current.
   Wait for the user to confirm or change the folder/category before generating questions
   or creating categories, topics or database records. Category confirmation is separate
   from question approval; never record it as approval of unseen questions.
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
