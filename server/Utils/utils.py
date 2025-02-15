import json as json_lib

class JSON_Tool:
    """
    Classe para manipulação de dados JSON.
    
    Atributos:
        json_data (str): Dados JSON em formato de string.
    
    Métodos:
        get(campo): Retorna o valor de um campo específico do JSON.
    """
    json_data: str
    
    def __init__(self, json_data: str):
        self.json_data = json_data

    def get(self, campo):
        try:
            return json_lib.loads(self.json_data)[campo]
        except Exception as e:
            raise ValueError(f"Não foi possível retornar o conteúdo do JSON {self.json_data}\n{str(e)}")

class File_Tool:
    """
    Classe para manipulação de arquivos.
    
    Atributos:
        file_name (str): Nome do arquivo a ser manipulado.
    
    Métodos:
        save(text): Salva um texto no arquivo especificado.
    """
    file_name: str
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def save(self, text):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(text)