from fastapi import HTTPException, status
from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Any

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
    
class IModel(ABC):
    """
    Interface para modelos de linguagem.
    
    Métodos:
        set_prompt(prompt: str): Define o prompt a ser utilizado pelo modelo.
        get() -> str: Retorna a resposta do modelo.
    
    Propriedades:
        nome (str): Retorna o nome da classe do modelo.
    """
    @abstractmethod
    def set_prompt(self, prompt: str):
        pass

    @abstractmethod
    def get(self) -> str:
        pass

    @property
    def nome(self) -> str:
        resultado = self.__class__.__name__
        return resultado