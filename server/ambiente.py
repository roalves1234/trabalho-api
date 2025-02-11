class Ambiente:
    model = None

    @staticmethod
    def model():
        return Ambiente.model

    @staticmethod
    def set_model(model):
        Ambiente.model = model