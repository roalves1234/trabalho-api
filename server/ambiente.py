class Ambiente:
    usuario = None
    llm_model = None

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
        
