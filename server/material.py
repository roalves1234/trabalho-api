from pydantic import BaseModel

class Material(BaseModel):
    """
    Classe que representa um material.
    
    Atributos:
        texto (str): Texto do material.
    
    Métodos:
        validar(): Valida se o campo texto está preenchido.
    """
    texto: str
    
    def validar(self):
        if not self.texto:
            raise Exception("O campo texto é obrigatório.")
