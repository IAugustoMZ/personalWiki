"""Validate a generate-questions round before it is presented or registered.

Usage:
    python questions/validate_questions.py <round.json> [--per-flavor N]

Exits 0 when every check passes, 1 otherwise. The reference and Markdown rules mirror
services/learning/question_import_validation.py in the timesheet back end (ADR-009); keep them in sync.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

FLAVORS = ("easy", "medium", "hard", "expert")
KINDS = ("concept", "code", "equation")
LETTERS = ("A", "B", "C", "D")

REFERENCE_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\b(note|nota|lab|laboratório|lesson|lição|section|seção|capítulo|chapter)\s*\d+",
        r"\.md\b",
        r"\b(the|this)\s+(sample|example|lab|lesson|notes?)\s+(above|below|table|data|shown|provided|given|that follows)\b",
        r"\baccording to (the|this)\s+(sample|example|data|notes?)\b",
        r"\b(the|this)\s+(course|module)\s+(notes?|material)\b",
    )
]
FENCE = re.compile(r"^\s*```", re.MULTILINE)
BLANK = "____"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def reference_hits(text: str) -> list[str]:
    return [m.group(0) for p in REFERENCE_PATTERNS for m in p.finditer(text)]


def markdown_errors(text: str) -> list[str]:
    problems: list[str] = []
    if len(FENCE.findall(text)) % 2:
        problems.append("unbalanced code fence (```)")
    without_fences = FENCE.sub("", text)
    if without_fences.count("$$") % 2:
        problems.append("unbalanced display math ($$)")
    inline = without_fences.replace("$$", "")
    if len(re.findall(r"(?<!\\)\$", inline)) % 2:
        problems.append("unbalanced inline math ($)")
    return problems


def check_question(q: dict, errors: list[str]) -> None:
    number = q.get("number")
    label = f"Q{number}"

    if q.get("difficulty") not in FLAVORS:
        errors.append(f"{label}: difficulty must be one of {FLAVORS}")
    if q.get("kind") not in KINDS:
        errors.append(f"{label}: kind must be one of {KINDS}")

    options = q.get("options")
    if not isinstance(options, dict) or sorted(options) != sorted(LETTERS):
        errors.append(f"{label}: options must be an object with keys A, B, C, D")
        options = {}
    values = [str(v).strip() for v in options.values()]
    if any(not v for v in values):
        errors.append(f"{label}: options must not be empty")
    if len({normalize(v) for v in values}) != len(values):
        errors.append(f"{label}: options must be distinct")
    if q.get("correct_option") not in LETTERS:
        errors.append(f"{label}: correct_option must be A, B, C or D")

    explanation = str(q.get("explanation", "")).strip()
    if not explanation:
        errors.append(f"{label}: explanation is empty")

    text = str(q.get("question_text", "")).strip()
    if not text:
        errors.append(f"{label}: question_text is empty")

    fields = {"question_text": text, "explanation": explanation}
    fields.update({f"option {k}": str(v) for k, v in options.items()})
    for field, value in fields.items():
        for hit in reference_hits(value):
            errors.append(f"{label}: {field} refers to material the learner cannot see: '{hit}'")
        for problem in markdown_errors(value):
            errors.append(f"{label}: {field}: {problem}")

    kind = q.get("kind")
    if kind == "code" and "```" not in text:
        errors.append(f"{label}: code questions need a fenced code block in question_text")
    if kind == "code" and BLANK not in text and not any(BLANK in str(v) for v in options.values()):
        errors.append(f"{label}: code questions need a blank marker ({BLANK}) or a name to recall")
    if kind == "equation" and not re.search(r"\$[^$]+\$|\$\$", text):
        errors.append(f"{label}: equation questions need LaTeX math in question_text")


def validate(data: dict, per_flavor: int | None) -> list[str]:
    errors: list[str] = []

    topic = data.get("topic", {})
    if not isinstance(topic.get("subsubcategory_id"), int):
        errors.append("topic.subsubcategory_id must be an integer")

    questions = data.get("questions")
    if not isinstance(questions, list) or not questions:
        return errors + ["questions must be a non-empty list"]

    numbers = [q.get("number") for q in questions]
    if len(set(numbers)) != len(numbers):
        errors.append("question numbers must be unique")

    for q in questions:
        check_question(q, errors)

    by_flavor = Counter(q.get("difficulty") for q in questions)
    if per_flavor is not None:
        for flavor in FLAVORS:
            if by_flavor[flavor] != per_flavor:
                errors.append(f"flavor {flavor}: expected {per_flavor} questions, found {by_flavor[flavor]}")
        minimum = max(1, math.ceil(0.2 * per_flavor))
        for flavor in FLAVORS:
            in_flavor = [q for q in questions if q.get("difficulty") == flavor]
            for kind in ("code", "equation"):
                found = sum(1 for q in in_flavor if q.get("kind") == kind)
                if found < minimum:
                    errors.append(
                        f"flavor {flavor}: needs at least {minimum} {kind} question(s), found {found}"
                    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", type=Path)
    parser.add_argument("--per-flavor", type=int, default=None, help="expected questions per flavor (n)")
    args = parser.parse_args()

    data = json.loads(args.path.read_text(encoding="utf-8"))
    errors = validate(data, args.per_flavor)
    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"OK: {len(data['questions'])} questions passed every check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
