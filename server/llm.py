from classes import IModel

class LLM:
    model: IModel = None

    def set_model(self, model: IModel) -> 'LLM':
        self.model = model
        return self

    def set_prompt(self, prompt: str) -> 'LLM':
        self.model.set_prompt(prompt)
        return self

    def go(self) -> str:
        return self.model.get()
