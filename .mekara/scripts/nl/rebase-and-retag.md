Rebase the current branch onto main, retag all commits with their original tags, and force push to GitHub.

<UserContext>$ARGUMENTS</UserContext>

## Process

### Step 0: Prepare for rebase

Check the current branch, update main, and return to the current branch:

```bash
current_branch=$(git branch --show-current)
git checkout main
git pull
git checkout "$current_branch"
```

### Step 1: Record commit mapping

Before rebasing, record the mapping between old commit hashes and their commit messages, and identify all tags on the branch:

```bash
git log --oneline --format='%H %s' main..HEAD > /tmp/old-commits.txt
git tag --list --format='%(refname:short) %(objectname:short)' | grep -E "$(git log --format='%h' main..HEAD | paste -sd '|' -)"
```

Save the tag-to-commit mapping for later. You'll need to know which tag goes with which commit message.

### Step 2: Rebase onto main

Run the rebase:

```bash
git rebase main
```

If conflicts occur, resolve them by:
1. Examining the conflict with `git status`
2. Understanding what changed in the target branch vs what the feature branch expects
3. Resolving in favor of the target branch's structural changes while preserving the feature branch's content additions
4. Staging resolved files with `git add`
5. Continuing with `git rebase --continue`

Repeat until rebase completes successfully.

### Step 3: Map tags to new commits

After the rebase, map each tag to its corresponding new commit by matching commit messages:

```bash
git log --oneline main..HEAD
```

For each tag that was on the old commits:
1. Find the new commit with the matching message
2. Force-update the tag: `git tag -f <tag-name> <new-commit-hash>`

### Step 4: Verify tags

Confirm all tags are correctly placed:

```bash
git log --oneline --decorate main..HEAD
```

### Step 5: Force push branch and tags

Push the rebased branch and updated tags to GitHub:

```bash
git push --force-with-lease origin "$current_branch"
git push --force origin <tag1> <tag2> <tag3> ...
```

Use `--force-with-lease` for the branch to ensure you don't accidentally overwrite changes pushed by someone else. Use `--force` for tags since they're being intentionally moved.

## Key Principles

- **Record before rebasing**: Always save commit hashes and tag information before rebasing, because rebase creates new commits with new hashes
- **Match by commit message**: After rebasing, use commit messages (which are preserved) to map old tags to new commits
- **Resolve conflicts structurally**: When rebasing onto a branch with structural changes (directory reorganization, etc.), adapt the feature branch's content to fit the new structure
- **Force push carefully**: Use `--force-with-lease` for branches to avoid overwriting unexpected changes; use `--force` for tags since you're intentionally moving them
