from __future__ import annotations

import argparse


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

    parser.parse_args()

    # When no arguments are provided, argparse will show help on -h/--help
    # For now, just print a simple message
    print("Hello from dojo!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
