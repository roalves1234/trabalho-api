from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from textwrap import dedent
from classes import Material
from llm import LLM
from ambiente import Ambiente
from model import Model
import jwt

SECRET_KEY = "UFG"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Dummy authentication, replace with actual validation
    if form_data.username != "admin" or form_data.password != "admin":
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/set_model")
def set_model(model_name: str, token: str = Depends(oauth2_scheme)):
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