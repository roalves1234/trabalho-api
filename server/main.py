from fastapi import FastAPI
from ambiente import Ambiente
from  llm_model import LLM_Model
from usuario import Usuario
from logger import Logger
import endpoints
import os

Ambiente.set_usuario(Usuario("admin", "admin"))
Ambiente.set_model(LLM_Model.ChatGPT())
Logger.get_instance().desativar()

app = FastAPI()
app.include_router(endpoints.router)


### incluir tipagem em todo o fonte.