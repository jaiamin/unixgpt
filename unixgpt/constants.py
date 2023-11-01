# ======================================================
# UnixGPT Default Values Collection
# ======================================================
#
# Default values used throughout the entire library.

import os

# Library version
VERSION: str = "0.1.0"

# OpenAI API key
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", None)
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required.")

# Default model for the library
DEFAULT_MODEL: str = "gpt-3.5-turbo"

# Current supported models
SUPPORTED_MODELS: list[str] = ["gpt-3.5-turbo"]