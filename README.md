# dojo

Dojo - A Python CLI tool

## Setup

Install dependencies using uv:

```bash
uv sync
```

Set up pre-commit hooks (for contributors):

```bash
uv run pre-commit install
```

## Usage

Run the CLI tool:

```bash
uv run dojo
```

Output:
```
Hello from dojo!
```

View help text:

```bash
uv run dojo --help
```

Output:
```
usage: dojo [-h] [--version]

Dojo - A Python CLI tool

options:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

For more information, visit the project repository.
```

## Testing

Run tests:

```bash
uv run pytest
```

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks automatically run on every commit and check:

- **Formatting**: Code is formatted with `ruff format`
- **Linting**: Code is linted with `ruff` (auto-fixes applied when possible)
- **Type-checking**: Code is type-checked with `mypy` in strict mode
- **Tests**: All tests pass with `pytest`

To manually run all hooks:

```bash
uv run pre-commit run --all-files
```
