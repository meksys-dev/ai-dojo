# AI Dojo

This file provides guidance to LLM agents when working with code in this repository.

## Project Overview

Dojo is a Python CLI tool built with argparse. The project uses `uv` as the package manager and build tool.

## Common Commands

```bash
# Install dependencies
uv sync

# Run the CLI
uv run dojo

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_sanity.py

# Run a specific test
uv run pytest tests/test_sanity.py::test_sanity

# Run all pre-commit hooks (formatting, linting, type-checking)
uv run pre-commit run --all-files

# Run individual checks
uv run ruff format .           # Format code
uv run ruff check --fix .      # Lint with auto-fix
uv run mypy --strict .         # Type-check
```

## Code Quality

- **Formatting**: ruff format
- **Linting**: ruff check (with auto-fix)
- **Type-checking**: mypy in strict mode

All new code must pass these checks. Pre-commit hooks run automatically on commit.

## Project Structure

- `src/dojo/` - Main package source code
  - `cli.py` - CLI entry point using argparse
  - `__init__.py` - Package version
- `tests/` - pytest test files
- `.github/workflows/` - CI workflows for pre-commit checks and tests

## Documentation

Documentation lives in an orphan `docs` branch. Contributors should set up a sibling worktree:
```bash
git worktree add ../docs docs
```
