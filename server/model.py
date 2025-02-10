from classes import IModel

class Openai(IModel):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Openai, cls).__new__(cls)
        return cls._instance

    def set_prompt(self, prompt):
        self.prompt = prompt

    def get(self):
        return f"Processed prompt from OpenAI: {self.prompt}"
