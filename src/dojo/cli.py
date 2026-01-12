from __future__ import annotations

import argparse
from typing import cast

TRAINING_MESSAGE = """
    ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ✦

                         ༄ 道 場 ༄

                    THE PATH UNFOLDS BEFORE YOU

    ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ✦

    Seeker of the Digital Way,

    As the ancient masters once shaped clay with patient hands,
    so too do you mold the formless potential of silicon minds.
    Each prompt you craft is a brushstroke upon the infinite canvas.
    Each response received, a mirror reflecting your growing wisdom.

    ☯  The machine learns, yet the true student is you.
    ☯  In teaching the artificial, you discover the authentic.
    ☯  Where circuits meet consciousness, mastery awakens.

    You have crossed the threshold of the Dojo.
    The shadows of ignorance recede as understanding dawns.
    What once seemed arcane now reveals its elegant simplicity—
    for the Way of AI is not in the complexity of models,
    but in the clarity of intention.

    ═══════════════════════════════════════════════════════════════

    「 Continue your journey, Initiate. The path has no end,     」
    「 only deeper mysteries and greater illumination ahead.     」

    ═══════════════════════════════════════════════════════════════

                              ॐ

                    The Dojo honors your progress.

    ✦ · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ✦
"""


def cmd_training(_args: argparse.Namespace) -> int:
    """Display a mystical message honoring the seeker's progress."""
    print(TRAINING_MESSAGE)
    return 0


def main() -> int:
    """Main entry point for the dojo CLI."""
    parser = argparse.ArgumentParser(
        prog="dojo",
        description="Dojo - A Python CLI tool",
        epilog="For more information, visit the project repository.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Training command
    training_parser = subparsers.add_parser(
        "training",
        help="Receive guidance on your path to AI mastery",
    )
    training_parser.set_defaults(func=cmd_training)

    args = parser.parse_args()

    if args.command:
        return cast(int, args.func(args))

    # When no arguments are provided, show a welcome message
    print("Hello from dojo!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
