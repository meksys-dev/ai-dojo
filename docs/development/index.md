# Development

This section covers development workflows and processes for contributors to the
Dojo project.

## Prerequisites

- Python 3.12 or higher
- `uv` package manager
  ([installation instructions](https://github.com/astral-sh/uv#installation))
- Git

## Repository Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/dojo.git
cd dojo/python
```

### Install Dependencies

Install all dependencies including development tools:

```bash
uv sync
```

This creates a virtual environment in `.venv/` and installs:

- Runtime dependencies (currently none)
- Development dependencies: mypy, pre-commit, pytest, ruff

### Set Up Pre-commit Hooks

Install the pre-commit hooks to run checks automatically on every commit:

```bash
uv run pre-commit install
```

## Development Workflows

### Running the CLI Locally

Run the CLI in development mode:

```bash
uv run dojo
```

This runs the CLI from the source code in `src/dojo/`.

### Code Quality Checks

Run all pre-commit hooks manually:

```bash
uv run pre-commit run --all-files
```

This runs:

- **ruff format** – Code formatting
- **ruff check** – Linting with auto-fixes
- **mypy** – Type checking in strict mode

You can also run individual checks:

```bash
# Format code
uv run ruff format .

# Lint with auto-fix
uv run ruff check --fix .

# Type-check
uv run mypy --strict .
```

### Running Tests

Run all tests with pytest:

```bash
uv run pytest
```

Run a specific test file:

```bash
uv run pytest tests/test_sanity.py
```

Run a specific test:

```bash
uv run pytest tests/test_sanity.py::test_sanity
```

## Continuous Integration

This project uses GitHub Actions for CI. All checks must pass before code can be
merged to `main`.

### Workflows

**Pre-commit Checks** (`.github/workflows/pre-commit.yml`)

- Runs all pre-commit hooks on every push and pull request
- Ensures code formatting, linting, and type-checking pass

**Tests** (`.github/workflows/tests.yml`)

- Runs the test suite with `pytest -v` on every push and pull request
- Validates all tests pass in a clean environment

### Branch Protection

The `main` branch is protected with:

- All CI checks must pass before merging
- Branches must be up-to-date with `main` before merging
- Linear history required (squash or rebase merge only)
- No force pushes allowed
- No direct commits to `main` (all changes via pull requests)
- Rules enforced for all users, including admins
- Merged branches are automatically deleted

## Documentation

Project documentation lives in the `docs` branch, an orphan branch with separate
history from the main codebase.

### Documentation Setup

AI agent commands and development workflows assume documentation is set up as a
sibling worktree:

```bash
# From the project root (python/), add the docs branch as a sibling worktree
git worktree add ../docs docs
```

This creates the following directory structure:

```
parent-directory/
├── python/          # main branch (this repo)
└── docs/            # docs branch worktree
```

With this setup, documentation can be edited alongside code without branch
switching.

### Building Documentation Locally

The documentation is built with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Navigate to the docs directory and serve the documentation:

```bash
cd ../docs  # If in python/
mkdocs serve
```

The documentation site will be available at `http://127.0.0.1:8000/`.

### Documentation Conventions

This project follows the
[standard Mekara documentation conventions](https://github.com/Meksys/mek/tree/main/project-scaffold-script/docs/docs/code-base/documentation/standard-mekara-docs.md).
Documentation is organized into:

- `usage/` – End-user documentation
- `development/` – Developer workflows (this section)
- `code-base/` – Implementation details and architecture
