from classes import IModel

class Ambiente:
    usuario: str
    llm_model: IModel

    @staticmethod
    def usuario():
        return Ambiente.usuario

    @staticmethod
    def llm_model():
        return Ambiente.llm_model

    @staticmethod
    def set_usuario(value):
        Ambiente.usuario = value
        
    @staticmethod
    def set_model(value):
        Ambiente.llm_model = value