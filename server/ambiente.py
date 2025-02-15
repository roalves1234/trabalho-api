from classes import ILLM_Model

class Ambiente:
    """
    A classe Ambiente é responsável por gerenciar o contexto do usuário e o modelo de linguagem (LLM).
    
    Atributos:
        usuario (str): Armazena o nome do usuário.
        llm_model (IModel): Armazena a instância do modelo de linguagem.

    Métodos:
        usuario() -> str: Retorna o nome do usuário.
        llm_model() -> IModel: Retorna a instância do modelo de linguagem.
        set_usuario(value: str): Define o nome do usuário.
        set_model(value: IModel): Define a instância do modelo de linguagem.
    """
    usuario: str
    llm_model: ILLM_Model

    @staticmethod
    def usuario() -> str:
        return Ambiente.usuario

    @staticmethod
    def llm_model() -> ILLM_Model:
        return Ambiente.llm_model

    @staticmethod
    def set_usuario(value: str):
        Ambiente.usuario = value
        
    @staticmethod
    def set_model(value: ILLM_Model):
        Ambiente.llm_model = value