from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from textwrap import dedent
from time import sleep
from classes import Material
from ambiente import Ambiente
from Utils.token_tool import Token
from Utils.logger import Logger
from Utils.utils import File_Tool
from llm import LLM
from llm_model import LLM_Model
from llm_work import LLM_Work
from file_work import File_Work

router = APIRouter()

@router.post("/get_token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    """
    Endpoint para obter um token de autenticação.
    
    Parâmetros:
    - form_data: Dados do formulário contendo nome de usuário e senha.
    
    Retorna:
    - Um dicionário contendo o token e o tipo de token.
    """
    if form_data.username != Ambiente.usuario.nome or form_data.password != Ambiente.usuario.senha:
        raise HTTPException(status_code=400, detail="Nome de usuário ou senha inválidos!")
    token = Token.criar(username_data={"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(Token.verificar)) -> dict:
    """
    Endpoint para definir o modelo de linguagem.
    
    Parâmetros:
    - model_name: Nome do modelo a ser definido.
    - token: Token de autenticação.
    
    Retorna:
    - Uma mensagem indicando o sucesso da operação.
    """
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
    """
    Endpoint para obter a conclusão de um texto.
    
    Parâmetros:
    - material: Objeto contendo o texto a ser completado.
    - token: Token de autenticação.
    
    Retorna:
    - Um dicionário contendo o texto original, a conclusão gerada e o nome do modelo utilizado.
    """
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