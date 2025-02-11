class LLM:
    def __init__(self):
        self.model = None

    def set_model(self, model):
        self.model = model
        return self

    def set_prompt(self, prompt):
        self.model.set_prompt(prompt)
        return self

    def go(self):
        return self.model.get()
