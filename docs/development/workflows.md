# Workflows

This page documents mekara slash commands available for this project.

## Git Operations

### `/rebase-and-retag`

Rebases the current branch onto main, retags all commits with their original
tags, and force pushes to GitHub.

Steps:

1. Check current branch, update main, and return to current branch
1. Record commit mapping (saves old commit hashes and tag information)
1. Rebase onto main, resolving any conflicts
1. Map tags to new commits by matching commit messages
1. Verify tags are correctly placed
1. Force push branch and tags to GitHub

Usage:

```
/rebase-and-retag
```

This command is useful when you need to rebase a branch that has tagged commits
(e.g., training/tutorial branches) while preserving all the tags on the rebased
commits.
