from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
from model import Model
from token_tool import Token

router = APIRouter()

@router.post("/get_token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()): # passado no body da requisição no formato x-www-form-urlencoded
    if form_data.username != "admin" or form_data.password != "admin":
        raise HTTPException(status_code=400, detail="Nome de usuário ou senha inválidos!")
    token = Token.criar(username_data={"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(Token.verificar)):
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