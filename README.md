#  🗣️ unixgpt

[![unixgpt](https://img.shields.io/badge/jamino30-unixgpt-<COLOR>?style=flat&color=blue)](https://github.com/jamino30/unixgpt)
[![pypi](https://img.shields.io/pypi/v/unixgpt)](https://pypi.org/project/unixgpt/)
[![image](https://img.shields.io/pypi/l/unixgpt)](https://pypi.python.org/pypi/unixgpt/)
[![image](https://img.shields.io/pypi/pyversions/unixgpt)](https://pypi.python.org/pypi/unixgpt/)
[![release](https://github.com/jamino30/unixgpt/actions/workflows/release.yml/badge.svg)](https://github.com/jamino30/unixgpt/actions/workflows/release.yml)
[![ruff](https://github.com/jamino30/unixgpt/actions/workflows/ruff.yml/badge.svg)](https://github.com/jamino30/unixgpt/actions/workflows/ruff.yml)

unixgpt is a powerful bridge between natural language and UNIX commands.

A valid OpenAI API Key is required to run unixgpt (you can get one here: https://openai.com/blog/openai-api)

```bash
export OPENAI_API_KEY="enter key here"
```

The latest version of ```unixgpt``` can be installed from PyPI:

```bash
pip install unixgpt
```

To upgrade to the latest version:

```bash
pip install --upgrade unixgpt
```

## Building Locally

### Docker

Build the Docker image

```bash
docker build -t unixgpt-cli .
```

Create and run the Docker container (with a valid OpenAI API Key)

```bash
docker run -e OPENAI_API_KEY unixgpt-cli
```

**Note:** Input can be edited in Dockerfile

### pip

Build via pip (from source code)

```bash
pip install .
```

Run via pip

```bash
unixgpt -i "enter input here"
```

## Features

1. **Conversion:** Seamlessly transform natural language queries into their corresponding UNIX commands.

2. **Command Options:** After generating a command, enjoy the following flexibility:

- **Execute:** Execute the generated UNIX command directly.
- **Save:** Store frequently used commands locally for swift and convenient access.
- **Copy:** Copy the generated command to the clipboard, simplifying pasting and use in your terminal.

3. **Reusability:** It's not just about storing commands; it's a versatile tool for saving and editing custom commands via natural language, ensuring your workflow remains flexible and efficient.

## Examples

### Conversion

![https://github.com/jamino30/unixgpt/blob/main/assets/demo.gif](https://github.com/jamino30/unixgpt/blob/main/assets/demo.gif)

```
Input: unixgpt -i "I want to see any uses of the 'git commit' command in my history"

Output: history | grep "git commit"
```

```
Input: unixgpt -i "Use the Dockerfile in the cwd to create an image called project-image"

Output: docker build -t project-image .
```

```
Input: unixgpt --input "Show me the current processes running on port 8000"

Output: lsof -i :8000
```

### Save

```
Input: unixgpt -s "git commit && git push"

Output: "Added to UnixGPT local library"
```

```
Input: unixgpt --save 1599

Output: "Added to UnixGPT local library"
```

### Fetch

```
Input: unixgpt -f "command that commits and pushes via Git"

Output: git commit && git push
```

```
Input: unixgpt --fetch 23

Output: "Returns command in UnixGPT local library with ID:23"
```
