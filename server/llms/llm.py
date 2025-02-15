from models.model_base import ILLM_Model

class LLM:
    """
    Classe para interação com modelos de linguagem.
    
    Atributos:
        model (IModel): Instância do modelo de linguagem.
    
    Métodos:
        set_model(model: IModel) -> LLM: Define o modelo de linguagem a ser utilizado.
        set_prompt(prompt: str) -> LLM: Define o prompt a ser utilizado pelo modelo.
        go() -> str: Executa o modelo de linguagem e retorna a resposta.
    """
    model: ILLM_Model = None

    def set_model(self, model: ILLM_Model) -> 'LLM':
        self.model = model
        return self

    def set_prompt(self, prompt: str) -> 'LLM':
        self.model.set_prompt(prompt)
        return self

    def go(self) -> str:
        return self.model.get()
