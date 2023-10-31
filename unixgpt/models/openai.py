import openai

import sys
sys.path.append("..")

from constants import OPENAI_API_KEY, DEFAULT_MODEL

from prompts import DEFAULT_PROMPT


class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.prices = {
            "gpt-3.5-turbo": 0.09
        }

    def fetch_unix_command(
            self, 
            user_input: str = "", 
            system_prompt: str = DEFAULT_PROMPT,
            model: str = DEFAULT_MODEL,
            temperature: float = 0,
            max_tokens: int = 250,
        ) -> str:
        
        unix_command: str = self._fetch_from_gpt(
            user_input=user_input,
            system_prompt=system_prompt,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        return unix_command.strip()

    def _fetch_from_gpt(
            self,
            user_input,
            system_prompt,
            model, 
            temperature,
            max_tokens,
        ) -> str:
        try:
            completion = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
        except Exception as e:
            print(e)
            
        try:
            result = completion.choices[0].message.content
        except KeyError as e:
            print(e)

        return result
    
    def _get_total_cost(
            self, 
            model,
            user_query, 
            system_prompt,
        ):
        return self.prices