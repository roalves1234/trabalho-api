from openai import OpenAI
import google.generativeai as genai
from classes import IModel
from config import Config
from ambiente import Ambiente

class LLM_Model:

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
                genai.configure(api_key=Config.google_api_key())
                cls._instance = super().__new__(cls)
                cls._client = genai.GenerativeModel(model_name="gemini-1.5-flash-002")
                
            return cls._instance

        def set_prompt(self, prompt):
            self.prompt = prompt

        def get(self):
            import json as json_lib
            
            resposta = self._client.generate_content([self.prompt]).text 
            try:
                json_lib.loads(resposta)
            except json_lib.JSONDecodeError:
                raise ValueError("JSON inválido - " + resposta)###
            
            return resposta
    
    class Factory: 
        @staticmethod
        def get(model_name):
            if model_name == "ChatGPT":
                return LLM_Model.ChatGPT()
            elif model_name == "Gemini":
                return LLM_Model.Gemini()
            else:
                raise ValueError(f"Nome de modelo inválido, informe ChatGPT ou Gemini.")