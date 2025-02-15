from fastapi import HTTPException, status
from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Any

class Material(BaseModel):
    texto: str
    
    def validar(self):
        if not self.texto:
            raise Exception("O campo texto é obrigatório.")
    
class IModel(ABC):
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