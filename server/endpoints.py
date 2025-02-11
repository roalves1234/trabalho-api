from fastapi import APIRouter
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
import model

router = APIRouter()

@router.post("/get_completion")
def get_completion(material: Material):
    resultado = LLM() \
                    .set_model(Ambiente.model) \
                    .set_prompt(dedent(f"""
                                        Complete o texto contido na tag <texto> e retorne um JSON com a resposta.
                                        
                                        <texto>
                                        {material.texto}
                                        </texto>
                                        """)) \
                    .go()
    return resultado

@router.post("/set_model")
def set_model(model: str):
    return {"message": "Modelo alterado com sucesso."}
