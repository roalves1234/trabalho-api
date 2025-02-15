from textwrap import dedent
from Utils.utils import JSON_Tool
from llms.llm import LLM
from ambiente import Ambiente

class LLM_Work:
    """
    Classe para manipulação de trabalhos com modelos de linguagem.
    
    Atributos:
        texto (str): Texto a ser utilizado no trabalho.
    
    Métodos:
        get_prompt() -> str: Retorna o prompt formatado para o modelo de linguagem.
        get_json_resposta() -> JSON_Tool: Retorna a resposta do modelo de linguagem em formato JSON.
        get() -> str: Retorna a resposta do modelo de linguagem.
    """
    texto: str = ""
    
    def __init__(self, texto: str):
        self.texto = texto

    def get_prompt(self) -> str:
        return dedent(f"""
                       # Input
                       - Um texto contido na tag <texto>.
                        
                       # Objetivo
                       - Completar o texto contido na tag <texto>.
                        
                       # A sua completação deve...
                       - Dar preferência ao que diz o senso comum.
                       - Ser coerente com o texto contido na tag <texto>.
                       - Só deve ultrapassar 1 linha se for realmente necessário para o sentido da frase como um todo.
                        
                       # Output: uma string JSON pura sem formatação, contendo este campo:
                       - completando: correspondente ao texto utilizado na completação.

                       <texto>
                       {self.texto}
                       </texto>
                       """)

    def get_json_resposta(self) -> JSON_Tool:
        return JSON_Tool(LLM() \
                            .set_model(Ambiente.llm_model) \
                            .set_prompt(self.get_prompt()) \
                            .go())

    def get(self) -> str:
        return self.get_json_resposta().get("completando")