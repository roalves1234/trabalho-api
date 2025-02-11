from fastapi import FastAPI
from dotenv import load_dotenv
from ambiente import Ambiente
from  model import Model
import endpoints
import os

load_dotenv()
app = FastAPI()
Ambiente.set_model(Model.ChatGPT())

app.include_router(endpoints.router)