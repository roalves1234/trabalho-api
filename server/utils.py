import json as json_lib

class JSON_Tool:
    def __init__(self, json_data):
        self.json_data = json_data

    def get(self, campo):
        try:
            return json_lib.loads(self.json_data)[campo]
        except Exception as e:
            raise ValueError(f"Não foi possível retornar o conteúdo do JSON {self.json_data}\n{str(e)}")

