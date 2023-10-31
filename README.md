# UnixGPT

UnixGPT is a powerful tool that facilitates the transformation of natural language into UNIX commands, making it a user-friendly bridge between the two.

## Features
1. Conversion: Effortlessly convert natural language queries into the corresponding UNIX commands.

2. Command Options: After generating a command, you have the flexibility to:
- Execute: Directly execute the generated UNIX command.
- Save: Store frequently used commands locally for quick and easy access
- Copy: Copy the generated command to the clipboard for easy pasting and use in your terminal.

3. Reusability: Once a command is saved, easily access the command from storage with natural language or by ID

## Running locally with Docker

- Ensure you have a valid OpenAI API Key (if not, get one here: https://openai.com/blog/openai-api)
- Build docker image

```bash
docker build -t unixgpt .
```

- Run docker container with specific configurations (OPENAI_API_KEY, USER_INPUT)

```bash
docker run -e USER_INPUT="Your custom input" -e OPENAI_API_KEY="Your key here" unixgpt
```
