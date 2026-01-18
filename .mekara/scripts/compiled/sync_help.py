"""Compiled mekara script: sync-help

Synchronize documentation (README, docs, etc.) with actual CLI help output when
they've drifted out of sync.
"""

from pathlib import Path
from typing import Generator

from mekara.scripting.runtime import (  # type: ignore[import-not-found]
    Auto,
    CallResult,
    LlmResult,
    ShellResult,
    auto,
    llm,
)


def _check_help_in_readme(help_text: str) -> bool:
    """Check if CLI help text appears in README.md.

    Returns:
        True if help text is found in README, False otherwise.
    """
    readme_path = Path("README.md")
    if not readme_path.exists():
        return False

    readme_content = readme_path.read_text()

    # Substring match - check if help output is present in README
    return help_text.strip() in readme_content


def _print_message(message: str) -> None:
    """Print a message to stdout."""
    print(message)


def execute(
    request: str,
) -> Generator[Auto, ShellResult | CallResult | LlmResult, None]:
    """Execute the sync-help script.

    Args:
        request: User request passed by mekara runtime (may be empty)
    """
    # Step 0: Get current CLI help output
    help_result = yield auto(
        "uv run dojo --help",
        context=(
            "Run `uv run dojo --help` and read README.md to identify "
            "discrepancies between the documented help text and the actual "
            "output."
        ),
    )

    # Step 1: Check if help text is in README
    check_result = yield auto(
        _check_help_in_readme,
        {"help_text": help_result.output},
        context=(
            "Run `uv run dojo --help` and read README.md to identify "
            "discrepancies between the documented help text and the actual "
            "output."
        ),
    )

    # Step 2: If discrepancies found, update documentation
    if not check_result.value:
        yield llm(
            "If discrepancies were found, edit the documentation file to "
            "replace the outdated help text with the current CLI output. "
            "Preserve the surrounding documentation structure.\n\n"
            "If no discrepancies were found, inform the user that "
            "documentation is already in sync.\n\n"
            "## Key Principles\n\n"
            "- **Source of truth is the code** - The CLI's actual output is "
            "authoritative; documentation should reflect it, not the other "
            "way around\n"
            "- **Preserve context** - Only update the help text block itself; "
            "don't restructure surrounding documentation unless asked\n"
            "- **Check for related drift** - If the help text changed, other "
            "examples in the doc (like sample command output) may also be "
            "stale"
        )
    else:
        # No discrepancies - inform user
        yield auto(
            _print_message,
            {"message": "Documentation is already in sync."},
            context=(
                "If no discrepancies were found, inform the user that "
                "documentation is already in sync."
            ),
        )
