class Usuario:
    nome: str = ""
    senha: str = ""
    
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha
