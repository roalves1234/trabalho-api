from textwrap import dedent
from time import sleep
from utils import JSON_Tool
from llm import LLM
from ambiente import Ambiente

class LLM_Work:
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
                       - Verifique se é necessário informar determinado caractere no início da completação, a fim de favorecer a concatenação do <texto> com a completação. Exemplo: <texto> = "Eu te" e completação = "amo". A completação tem que ficar como " amo" (1 espaço antes) para favorecer a concatenação, ficando assim: "Eu te amo".
                        
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

    def save(self, text):
        with open('output.md', 'w', encoding='utf-8') as f:
            f.write(text)

    def get(self) -> str:
        self.save(f"# {self.texto}")
        sleep(1)

        completando = self.get_json_resposta().get("completando")
        self.save(f"# {self.texto} {completando}")

        return completando