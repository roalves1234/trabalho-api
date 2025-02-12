from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
from model import Model
import jwt
from jwt import PyJWTError

SECRET_KEY = "UFG"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

def criar_token(username_data: dict):
    to_encode = username_data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido!")
        return username
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido!!")

@router.post("/get_token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends()): # passado no body da requisição no formato x-www-form-urlencoded
    if form_data.username != "admin" or form_data.password != "admin":
        raise HTTPException(status_code=400, detail="Nome de usuário ou senha inválidos!")
    token = criar_token(username_data={"sub": form_data.username})
    return {"token": token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(verificar_token)):
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