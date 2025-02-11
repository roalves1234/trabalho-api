from fastapi import HTTPException, status
from pydantic import BaseModel
from abc import ABC, abstractmethod

class Material(BaseModel):
    texto: str
    def validar(self):
        if not self.texto:
            raise Exception("O campo texto é obrigatório.")
    
class IModel(ABC):
    @abstractmethod
    def set_prompt(self, prompt):
        pass

    @abstractmethod
    def get(self):
        pass