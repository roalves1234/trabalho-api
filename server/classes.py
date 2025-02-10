from fastapi import HTTPException, status
from pydantic import BaseModel
from abc import ABC, abstractmethod

class Material(BaseModel):
    texto: str
    
class IModel(ABC):
    @abstractmethod
    def set_prompt(self, prompt):
        pass

    @abstractmethod
    def get(self):
        pass