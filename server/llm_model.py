from openai import OpenAI
import google.generativeai as genai
from classes import IModel
from config import Config
from ambiente import Ambiente

class LLM_Model:

    class ChatGPT(IModel):
        _instance: 'LLM_Model.ChatGPT' = None 
        _client: OpenAI = None
        prompt: str = ""

        def __init__(self):
            self._client = OpenAI(api_key = Config.openai_api_key())

        @staticmethod
        def get_instance() -> 'LLM_Model.ChatGPT':
            if LLM_Model.ChatGPT._instance is None:
                LLM_Model.ChatGPT._instance = LLM_Model.ChatGPT()
            return LLM_Model.ChatGPT._instance

        def set_prompt(self, prompt):
            self.prompt = prompt

        def get(self) -> str:
            resposta = self._client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": "Você é um assistente muito eficiente."},
                                {"role": "user", "content": self.prompt}
                            ]).choices[0].message.content
            return resposta

    class Gemini(IModel):
        _instance: 'LLM_Model.Gemini' = None 
        _client: genai.GenerativeModel = None
        prompt: str

        def __init__(self):
            genai.configure(api_key=Config.google_api_key())
            self._client = genai.GenerativeModel(model_name="gemini-1.5-flash-002")

        @staticmethod
        def get_instance() -> 'LLM_Model.Gemini':
            if LLM_Model.Gemini._instance is None:
                LLM_Model.Gemini._instance = LLM_Model.Gemini()
            return LLM_Model.Gemini._instance

        def set_prompt(self, prompt):
            self.prompt = prompt

        def get(self) -> str:
            resposta = self._client.generate_content([self.prompt]).text 
            return resposta
    
    class Factory:
        @staticmethod
        def get(model_name: str) -> IModel:
            if model_name == "ChatGPT":
                return LLM_Model.ChatGPT.get_instance()
            elif model_name == "Gemini":
                return LLM_Model.Gemini.get_instance()
            else:
                raise ValueError(f"Nome de modelo inválido, informe ChatGPT ou Gemini.")