from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    @staticmethod
    def openai_api_key() -> str:
        return os.getenv("OPENAI_API_KEY")

    @staticmethod
    def google_api_key() -> str:
        return os.getenv("GOOGLE_API_KEY")