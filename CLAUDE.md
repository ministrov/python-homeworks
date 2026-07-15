# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Personal Python homework/practice repository (split off from a separate main
repo). Each top-level folder is a standalone exercise, numbered in the order
it was completed — there is no shared package, build system, or test suite.
Run any file directly:

```
python <folder>/<file>.py
python <folder>/<file>.py <cli-args>   # 5_library expects sys.argv
```

Target interpreter is Python 3.14 (`python --version`). No dependency
manager, requirements file, or virtualenv is checked in — stdlib only so far.

## Repository structure

- `1_vars/` — variables, input/print basics.
- `2_operations/` — numeric operations, lists/tuples (`expences.py`,
  `discount.py`).
- `3_menu/` — control flow, `match`/`case`.
- `4_expenses/` — loop-driven interactive CLI menu over a `list[float]`
  (`menu.py` is the entry point; `expenses.py`/`strings.py` hold earlier
  variants).
- `5_library/` — CLI script driven by `sys.argv` (`action`, `argument`)
  implementing `filter`/`sort` over a `dict[str, str]` catalog. `PLAN.md` in
  that folder is a step-by-step design doc with a checklist — read it before
  changing `library.py` to see what's intentionally done vs. still open.
- `6_crm/` — the most structured exercise so far, split into modules:
  - `orders.py` — domain model (`Order` as `TypedDict`, `OrderStatus` as
    `Literal`) and pure functions (`create_order`, `list_orders`,
    `edit_order`, `remove_order`) operating on `list[Order]`.
  - `storage.py` — JSON persistence (`load`/`save`), currently stubbed
    (`pass`) — not yet implemented.
  - `cli.py` — command/argument parsing, currently just a stub docstring.
  - `utils/validators.py` — id/field validation, currently just a stub
    docstring.
  - `__main__.py` — entry point wiring the pieces together; run as
    `python 6_crm/__main__.py` (imports are unqualified — run from inside
    `6_crm/`, not from repo root, until it's turned into a proper package).

Folders are additive history, not a curriculum tree to keep refactoring —
earlier exercises (`1_vars` … `4_expenses`) are done and generally
shouldn't be rewritten except to fix a real bug.

## Conventions observed in the code

- Docstrings at the top of each script restate the assignment (in Russian)
  — keep that pattern when adding new exercise files.
- Type hints are used consistently on function signatures
  (`list[float]`, `dict[str, str]`, `TypedDict`, `Literal`), aimed at
  passing Pylance strict mode. Match this level of typing in new code.
- Comments/strings/prompts are in Russian; keep new exercise code
  consistent with that.
- `6_crm` favors small pure functions over classes, `KeyError` for
  not-found/invalid-field cases, and a module-level `_PRIVATE` constant
  (`_EDITABLE_FIELDS`) for internal allowlists.

## Skills configured in this repo

- **`/senior-backend`** — acts as a senior-dev mentor for the repo owner
  (currently at intern/стажёр level, not Junior). Use it when reviewing
  completed exercises, planning the next topic, or auditing repo quality.
  It expects `PROGRESS.md` / roadmap files to track learning progress —
  those don't exist yet in this repo, only in the skill's own template.
- **`/commit`** — Conventional Commits format for this repo: type from
  `feat|fix|refactor|docs|style|test|chore|perf|ci|build`, lowercase
  subject ≤72 chars, optional 2–6 bullet body, scope = folder/area
  touched. Commit as the configured git user — never attribute commits to
  Claude/add a Co-Authored-By trailer.
