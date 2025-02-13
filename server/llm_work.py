from textwrap import dedent
from utils import JSON_Tool
from llm import LLM
from ambiente import Ambiente

class LLM_Work:
    def __init__(self, texto: str):
        self.texto = texto

    def get_prompt(self) -> str:
        return dedent(f"""
                       # Input
                       - Um texto contido na tag <texto>
                        
                       # Objetivo
                       - Completar o texto contido na tag <texto>
                        
                       # A sua completação deve...
                       - Dar preferência ao que diz o senso comum
                       - Ser coerente com o texto contido na tag <texto>
                       - Só deve ultrapassar 1 linha se for realmente necessário para o sentido da frase como um todo
                       - Respeitar a pontuação para continuar de forma coerente a frase inicial
                        
                       # Output: uma string JSON pura sem formatação, contendo este campo:
                       - completando: correspondente ao texto utilizado na completação.

                       <texto>
                       {self.texto}
                       </texto>
                       """)

    def get_json_resposta(self):
        return JSON_Tool(LLM() \
                            .set_model(Ambiente.llm_model) \
                            .set_prompt(self.get_prompt()) \
                            .go())

    def get(self) -> str:
        return self.get_json_resposta().get("completando")