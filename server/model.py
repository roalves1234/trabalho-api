from classes import IModel
from openai import OpenAI
from config import Config
from ambiente import Ambiente

class Model:

    class ChatGPT(IModel):
        _instance = None 
        _client = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._client = OpenAI(api_key = Config.openai_api_key())
            return cls._instance

        def set_prompt(self, prompt):
            self.prompt = prompt

        def get(self):
            return self._client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um assistente muito eficiente."},
                        {"role": "user", "content": self.prompt}
                    ]).choices[0].message.content

    class Gemini(IModel):
        _instance = None 
        _client = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._client = OpenAI(api_key = Config.openai_api_key())
            return cls._instance

        def set_prompt(self, prompt):
            self.prompt = prompt

        def get(self):
            return self._client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um assistente muito eficiente."},
                        {"role": "user", "content": self.prompt}
                    ]).choices[0].message.content
    
    class Factory: ###
        @staticmethod
        def get(model_name):
            if model_name == "ChatGPT":
                return Model.ChatGPT()
            elif model_name == "Gemini":
                return Model.Gemini()
            else:
                raise ValueError(f"Nome de modelo inválido, informe ChatGPT ou Gemini.")