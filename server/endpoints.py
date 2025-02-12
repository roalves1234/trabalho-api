from fastapi import APIRouter, HTTPException
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
from  model import Model

router = APIRouter()

@router.post("/set_model")
def set_model(model_name: str):
    try:
        Ambiente.set_model(Model.Factory.get(model_name))
        return {"message": f"Modelo alterado com sucesso para {model_name}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/get_completion")
def get_completion(material: Material):
    try:
        material.validar()
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
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))