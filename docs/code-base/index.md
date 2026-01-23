# Code-base

This section provides a navigation guide to the Dojo codebase for contributors
and maintainers.

## Repository Structure

Dojo uses a dual-branch worktree structure to separate code from documentation:

- **`main` branch** (`python/` directory) – The Python CLI project
- **`docs` branch** (`docs/` directory) – The documentation site

This allows documentation to be edited alongside code without branch switching,
while keeping their git histories completely separate.

## Worktree Setup

The repository is designed to be used with git worktrees. Contributors should
set up a sibling worktree for the documentation:

```bash
# From the main branch (python/), add the docs branch as a sibling worktree
git worktree add ../docs docs
```

This creates the following directory structure:

```
parent-directory/
├── python/          # main branch
│   ├── src/
│   ├── tests/
│   └── ...
└── docs/            # docs branch worktree
    ├── docs/
    ├── mkdocs.yml
    └── ...
```

### Why This Structure?

**Separate histories**: The `docs` branch is an orphan branch with no shared
history with `main`. This keeps documentation commits separate from code
commits, making the git history cleaner and more focused.

**No branch switching**: With the worktree setup, you can edit code in `python/`
and documentation in `docs/` simultaneously without switching branches.

**AI agent compatibility**: Development workflows and AI agent commands assume
this structure is in place, with documentation accessible at `../docs` relative
to the Python project.

## Navigation

This code-base section is divided into two main areas:

- **[Dojo](dojo.md)** – The main Python CLI project structure, architecture, and
  implementation details
- **[Documentation](documentation.md)** – The documentation site structure,
  configuration, and maintenance

Each page provides implementation details and navigation aids for working with
that part of the project.
