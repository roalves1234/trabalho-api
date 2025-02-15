from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from textwrap import dedent
from time import sleep
from classes import Material
from ambiente import Ambiente
from token_tool import Token
from logger import Logger
from utils import File_Tool
from llm import LLM
from llm_model import LLM_Model
from llm_work import LLM_Work
from file_work import File_Work

router = APIRouter()

@router.post("/get_token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict: # passado no body da requisição no formato x-www-form-urlencoded
    if form_data.username != Ambiente.usuario.nome or form_data.password != Ambiente.usuario.senha:
        raise HTTPException(status_code=400, detail="Nome de usuário ou senha inválidos!")
    token = Token.criar(username_data={"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(Token.verificar)) -> dict:
    Logger.get_instance().set(f"/set_model: model_name = {model_name}")
    try:
        Ambiente.set_model(LLM_Model.Factory.get(model_name))
        Logger.get_instance().set("/set_model: alteração ok")
        
        return {"message": f"Modelo alterado com sucesso para {model_name}"}
    except Exception as e:
        Logger.get_instance().set(f"/set_model: erro = {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/get_completion")
def get_completion(material: Material, token: str = Depends(Token.verificar)) -> dict:
    try:
        material.validar()

        file_work = File_Work()
        file_work.do_texto(material.texto)

        completando = LLM_Work(material.texto).get()
        resultado = {"texto": material.texto,
                    "completando": completando,
                    "model": Ambiente.llm_model.nome}

        file_work.do_completando(completando)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))