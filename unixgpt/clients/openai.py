import openai

import sys
sys.path.append("..")

from constants import OPENAI_API_KEY, DEFAULT_MODEL
from prompts import OPENAI_PROMPT

class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.prompt = OPENAI_PROMPT

    def get_unix_command(
            self, 
            user_input: str, 
            model: str = DEFAULT_MODEL,
            temperature: float = 0,
            max_tokens: int = 250
        ):
        
        completion = openai.ChatCompletion.create(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": user_input}
            ]
        )
        unix_command: str = completion.choices[0].message.content
        
        return unix_command.strip()