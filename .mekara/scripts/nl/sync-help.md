Synchronize CLI help text documentation with actual CLI output to ensure README accuracy.

<UserContext></UserContext>

## Process

### Step 0: Gather information

Gather the following information from the user-provided context:
- which CLI tool's help text needs to be checked (default: the main project CLI)
- which documentation file contains the help text (default: README.md)

If any information is unclear or missing, ask the user for details.

### Step 1: Capture the current CLI help output

Run the CLI tool with the `--help` flag to capture its current output.

### Step 2: Compare with documented help text

Read the documentation file and locate the section that documents the help text. Compare it with the actual output from Step 1 to identify any discrepancies.

### Step 3: Update the documentation

If discrepancies exist, update the documentation file to match the actual CLI output. Preserve the documentation structure (code blocks, formatting, section headers) while replacing the outdated help text with the current version.

## Key Principles

- **Documentation follows code**: The documentation should always reflect the actual behavior of the CLI, not an aspirational or outdated version
- **Complete help text**: Include all elements from the help output (usage line, subcommands, positional arguments, options, footer text)
- **Preserve formatting**: Keep the documentation's markdown structure intact while updating the content within code blocks
