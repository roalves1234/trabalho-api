from fastapi import FastAPI
from ambiente import Ambiente
from  llms.llm_model import LLM_Model
from models.usuario import Usuario
from Utils.logger import Logger
import endpoints
import os

Logger.get_instance().desativar()
Ambiente.set_usuario(Usuario("admin", "admin"))
Ambiente.set_model(LLM_Model.ChatGPT())

app = FastAPI()
app.include_router(endpoints.router) 