from fastapi import APIRouter
from classes import Material
from llm import LLM
import model

router = APIRouter()

@router.post("/get_completion")
def get_completion(material: Material):
    resultado = LLM() \
                    .set_model(model.Openai()) \
                    .set_prompt(f"""
                                Complete o texto contido na tag <texto> e retorne um JSON com a resposta.
                                
                                <texto>
                                {material.texto}
                                </texto>
                                """) \
                    .go()
    return resultado
