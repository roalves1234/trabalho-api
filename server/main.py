from fastapi import FastAPI
from dotenv import load_dotenv
import endpoints
import os

load_dotenv()
app = FastAPI()

app.include_router(endpoints.router)