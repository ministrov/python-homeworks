# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Personal Python homework/practice repository (split off from a separate main
repo), split by course difficulty level into `basic/`, `intermediate/`, and
`advanced/`. Within each level, top-level folders are standalone exercises,
numbered in the order they were completed — there is no shared package,
build system, or test suite. Run any file directly:

```
python <level>/<folder>/<file>.py
python basic/5_library/library.py <cli-args>   # 5_library expects sys.argv
```

Target interpreter is Python 3.14 (`python --version`). No dependency
manager, requirements file, or virtualenv is checked in — stdlib only so far.

## Repository structure

### `basic/`

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
- `6_crm/` — a finished CLI utility for managing orders, split into modules:
  - `orders.py` — domain model (`Order` as `TypedDict`, `OrderStatus` as
    `Literal`) and pure functions operating on `list[Order]`: `new_order`
    (generates a uuid4 id), `create_order`, `list_orders`, `find_order`
    (raises `KeyError` if missing), `edit_order` (only fields in
    `_EDITABLE_FIELDS` allowed, `KeyError` otherwise), `remove_order`,
    `add_tags`/`remove_tags`, `set_status` (also stamps `closed_at`),
    `is_overdue`, `filter_by_tag`/`filter_overdue`.
  - `storage.py` — JSON persistence (`load`/`save`); tags are stored as a
    list on disk and converted to/from `set[str]` in memory.
  - `cli.py` — one `parse_<command>` function per subcommand (`list`,
    `add`, `remove`, `edit`, `tags`, `status`), each a manual `while`-loop
    scan of the args list (no `argparse`) returning a plain tuple of
    typed values.
  - `utils/validators.py` — `validate_email`, `validate_amount`,
    `validate_status`, `parse_tags`.
  - `utils/table.py` — `print_orders`, the table-printing helper for
    `list` output; kept separate from `validators.py` since that module
    is scoped to validation only.
  - `__main__.py` — entry point: dispatches on `sys.argv[1]` to one
    `run_<command>` function per command (parse → validate → call the
    domain function → save → print). Run as
    `python __main__.py <command> [flags]` (imports are
    unqualified — run from inside `basic/6_crm/`, not from repo root, until
    it's turned into a proper package).

  Commands: `list` (`--overdue`, `--tag`, `--limit`), `add` (`--title`,
  `--amount`, `--email`, `--due`, `--tags`), `remove` (`--id`), `edit`
  (`--id` plus any of `--title`/`--amount`/`--email`/`--due`), `tags`
  (`--id`, `--add`, `--remove`), `status` (`--id` plus a positional
  status value).

  Deliberately kept to plain loops, `if`/`elif`, and manual `sys.argv`
  parsing instead of `argparse`, comprehensions, `cast()`, or set-operator
  shortcuts (`|=`/`-=`) — the repo owner asked for code that reads as
  intern/junior-level rather than idiomatic-but-denser Python. Preserve
  that style in further `6_crm` edits unless told otherwise. One
  `# type: ignore[arg-type]` remains in `__main__.py`'s `status` command,
  bridging a runtime-validated `str` to the `OrderStatus` `Literal` type
  without reaching for `typing.cast`.

Folders are additive history, not a curriculum tree to keep refactoring —
earlier exercises (`basic/1_vars` … `basic/4_expenses`) are done and
generally shouldn't be rewritten except to fix a real bug.

### `intermediate/`

- `1_oop/` — OOP exercises. `basic_oop.py` is currently an empty
  placeholder — not yet started.

### `advanced/`

Empty so far (holds only `.gitkeep`); reserved for the advanced-level
course track.

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
