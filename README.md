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
usage: dojo [-h] [--version] {training} ...

Dojo - A Python CLI tool

positional arguments:
  {training}  Available commands
    training  Receive guidance on your path to AI mastery

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

To manually run all hooks:

```bash
uv run pre-commit run --all-files
```

Note: Tests are run in CI, not as pre-commit hooks, to keep commits fast.

## Continuous Integration

This repository uses GitHub Actions for continuous integration. All checks must pass before code can be merged to `main`.

### Workflows

**Pre-commit Checks** (`.github/workflows/pre-commit.yml`)
- Runs all pre-commit hooks on every push and pull request
- Ensures code formatting, linting, and type-checking pass

**Tests** (`.github/workflows/tests.yml`)
- Runs the test suite with `pytest -v` on every push and pull request
- Validates all tests pass in a clean environment

### Branch Protection

The `main` branch is protected with the following rules:

- ✅ All CI checks must pass before merging
- ✅ Branches must be up-to-date with `main` before merging
- ✅ Linear history required (squash or rebase merge only)
- ✅ No force pushes allowed
- ✅ No direct commits to `main` (all changes via pull requests)
- ✅ Rules enforced for all users, including admins
- ✅ Merged branches are automatically deleted

## Documentation

Project documentation lives in the `docs` branch, an orphan branch with separate history from the main codebase.

### Local Setup for Contributors

AI agent commands and development workflows assume documentation is set up as a sibling worktree:

```bash
# From the project root, add the docs branch as a sibling worktree
git worktree add ../docs docs
```

This creates the following directory structure:

```
parent-directory/
├── python/          # main branch (this repo)
└── docs/            # docs branch worktree
```

With this setup, documentation can be edited alongside code without branch switching.
