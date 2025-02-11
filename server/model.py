from classes import IModel
from openai import OpenAI
from config import Config

class Openai(IModel):
    _instance = None

    def __init__(self):
        self.client = OpenAI(api_key = Config.openai_api_key())

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Openai, cls).__new__(cls)
        return cls._instance

    def set_prompt(self, prompt):
        self.prompt = prompt

    def get(self):
        return self.client.chat.completions.create(
                   model="gpt-4o-mini",
                   messages=[
                       {"role": "system", "content": "Você é um assistente muito eficiente."},
                       {"role": "user", "content": self.prompt}
                   ]).choices[0].message.content
