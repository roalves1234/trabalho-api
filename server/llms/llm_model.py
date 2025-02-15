from openai import OpenAI
import google.generativeai as genai
from model_base import ILLM_Model
from llms.llm_api_key import LLM_API_Key
from ambiente import Ambiente

class LLM_Model:
    """
    Classe para gerenciamento de diferentes modelos de linguagem.
    
    Subclasses:
        ChatGPT: Implementação do modelo ChatGPT.
        Gemini: Implementação do modelo Gemini.
        Factory: Fábrica para criação de instâncias de modelos de linguagem.
    """
    class ChatGPT(ILLM_Model):
        """
        Implementação do modelo ChatGPT.
        
        Atributos:
            _instance (LLM_Model.ChatGPT): Instância única da classe ChatGPT.
            _client (OpenAI): Cliente da API OpenAI.
            prompt (str): Prompt a ser utilizado pelo modelo.
        
        Métodos:
            get_instance() -> LLM_Model.ChatGPT: Retorna a instância única da classe ChatGPT.
            set_prompt(prompt): Define o prompt a ser utilizado pelo modelo.
            get() -> str: Retorna a resposta do modelo ChatGPT.
        """
        _instance: 'LLM_Model.ChatGPT' = None 
        _client: OpenAI = None
        prompt: str = ""

        def __init__(self):
            self._client = OpenAI(api_key = LLM_API_Key.openai())

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

    class Gemini(ILLM_Model):
        """
        Implementação do modelo Gemini.
        
        Atributos:
            _instance (LLM_Model.Gemini): Instância única da classe Gemini.
            _client (genai.GenerativeModel): Cliente da API Generative AI.
            prompt (str): Prompt a ser utilizado pelo modelo.
        
        Métodos:
            get_instance() -> LLM_Model.Gemini: Retorna a instância única da classe Gemini.
            set_prompt(prompt): Define o prompt a ser utilizado pelo modelo.
            get() -> str: Retorna a resposta do modelo Gemini.
        """
        _instance: 'LLM_Model.Gemini' = None 
        _client: genai.GenerativeModel = None
        prompt: str

        def __init__(self):
            genai.configure(api_key=LLM_API_Key.google())
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
        """
        Fábrica para criação de instâncias de modelos de linguagem.
        
        Métodos:
            get(model_name: str) -> IModel: Retorna a instância do modelo de linguagem especificado.
        """
        @staticmethod
        def get(model_name: str) -> ILLM_Model:
            if model_name == "ChatGPT":
                return LLM_Model.ChatGPT.get_instance()
            elif model_name == "Gemini":
                return LLM_Model.Gemini.get_instance()
            else:
                raise ValueError(f"Nome de modelo inválido, informe ChatGPT ou Gemini.")