from fastapi import FastAPI
from dotenv import load_dotenv
from ambiente import Ambiente
from  llm_model import LLM_Model
from usuario import Usuario
import endpoints
import os

load_dotenv()
app = FastAPI()
Ambiente.set_usuario(Usuario("admin", "admin"))
Ambiente.set_model(LLM_Model.Gemini())


app.include_router(endpoints.router)


### incluir tipagem em todo o fonte.