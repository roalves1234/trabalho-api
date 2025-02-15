from classes import IModel

class Ambiente:
    usuario: str
    llm_model: IModel

    @staticmethod
    def usuario() -> str:
        return Ambiente.usuario

    @staticmethod
    def llm_model() -> IModel:
        return Ambiente.llm_model

    @staticmethod
    def set_usuario(value: str):
        Ambiente.usuario = value
        
    @staticmethod
    def set_model(value: IModel):
        Ambiente.llm_model = value