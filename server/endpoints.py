from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
from llm_model import LLM_Model
from token_tool import Token

router = APIRouter()

@router.post("/get_token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()): # passado no body da requisição no formato x-www-form-urlencoded
    if form_data.username != Ambiente.usuario.nome or form_data.password != Ambiente.usuario.senha:
        raise HTTPException(status_code=400, detail="Nome de usuário ou senha inválidos!")
    token = Token.criar(username_data={"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(Token.verificar)):
    try:
        Ambiente.set_model(LLM_Model.Factory.get(model_name))
        return {"message": f"Modelo alterado com sucesso para {model_name}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/get_completion")
def get_completion(material: Material, token: str = Depends(Token.verificar)):
    try:
        material.validar()
        resposta = LLM() \
                    .set_model(Ambiente.llm_model) \
                    .set_prompt(dedent(f"""
                                        # Input
                                        - Um texto contido na tag <texto>
                                        
                                        # Objetivo
                                        - Completar o texto contido na tag <texto>
                                        
                                        # Como fazer a completação
                                        - Dê preferência ao que diz o senso comum
                                        
                                        # Output: uma string JSON pura sem formatação, contendo este campo:
                                        - completando: correspondente ao texto utilizado na completação.

                                        <texto>
                                        {material.texto}
                                        </texto>
                                        """)) \
                    .go()
        ###
        import json as json_lib
        try:
            completando = json_lib.loads(resposta)["completando"]
            print(completando)
        except json_lib.JSONDecodeError:
            raise ValueError("JSON inválido - " + resposta)###
        ###
        return {"texto": material.texto,
                "completando": completando,
                "model": Ambiente.llm_model.__class__.__name__}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))