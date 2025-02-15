from dotenv import load_dotenv
import os

load_dotenv()

class LLM_API_Key:
    """
    Classe para gerenciamento de configurações.
    
    Métodos:
        openai() -> str: Retorna a chave da API OpenAI.
        google() -> str: Retorna a chave da API Google.
    """
    @staticmethod
    def openai() -> str:
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def google() -> str:
        return os.getenv("GOOGLE_API_KEY")