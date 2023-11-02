# unixgpt

[![PyPI](https://img.shields.io/pypi/v/unixgpt)](https://pypi.org/project/unixgpt/)
[![Upload Python Package](https://github.com/jamino30/unixgpt/actions/workflows/python-publish.yml/badge.svg)](https://github.com/jamino30/unixgpt/actions/workflows/python-publish.yml)

unixgpt is a powerful bridge between natural language and UNIX commands.

![https://github.com/jamino30/unixgpt/blob/main/assets/demo.gif](https://github.com/jamino30/unixgpt/blob/main/assets/demo.gif)

The latest version of ```unixgpt``` can be installed from PyPI:

```bash
pip install unixgpt
```

To upgrade to the latest version:

```bash
pip install --upgrade unixgpt
```

## Features
1. Conversion: Effortlessly convert natural language queries into the corresponding UNIX commands.

2. Command Options: After generating a command, you have the flexibility to:
- Execute: Directly execute the generated UNIX command.
- Save: Store frequently used commands locally for quick and easy access
- Copy: Copy the generated command to the clipboard for easy pasting and use in your terminal.

3. Reusability: Once a command is saved, easily access the command from storage with natural language or by ID

## Examples

### Conversion

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
