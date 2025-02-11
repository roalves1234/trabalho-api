from fastapi import FastAPI
from dotenv import load_dotenv
from ambiente import Ambiente
import model
import endpoints
import os

load_dotenv()
app = FastAPI()
Ambiente.set_model(model.Openai())

app.include_router(endpoints.router)