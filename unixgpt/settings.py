import os

VERSION: str = "0.1.0"

OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", None)

DEFAULT_MODEL: str = "gpt-3.5-turbo"

SUPPORTED_MODELS: list[str] = ["gpt-3.5-turbo"]