# Usage

This section covers how to install and use Dojo as an end user.

## Installation

### Using uv (Recommended)

If you have `uv` installed, you can add Dojo to your project:

```bash
uv add dojo
```

### Using pip

Alternatively, install with pip:

```bash
pip install dojo
```

### From Source

Clone the repository and install:

```bash
git clone https://github.com/yourusername/dojo.git
cd dojo/python
uv sync
```

## Running Dojo

Once installed, run the CLI tool:

```bash
dojo
```

Output:

```
Hello from dojo!
```

## Command-Line Options

View all available options:

```bash
dojo --help
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

### `--version`

Display the current version of Dojo:

```bash
dojo --version
```

Output:

```
dojo 0.1.0
```

## Common Workflows

### Basic Usage

Currently, Dojo is a minimal scaffold. When run without arguments, it prints a
greeting message. Future versions will add more functionality.
