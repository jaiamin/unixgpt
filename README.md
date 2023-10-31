# UnixGPT

UnixGPT seamlessly bridges the gap between natural language and UNIX commands.

## Running locally with Docker

- Ensure you have a valid OpenAI API Key (if not, get one here: https://openai.com/blog/openai-api)
- Build docker image

```bash
docker build -t unixgpt .
```

- Run docker container with specific configurations (OPENAI_API_KEY, USER_INPUT)

```bash
docker run -e USER_INPUT="Your custom input" -e OPEN_API_KEY="Your key here" unixgpt
```
