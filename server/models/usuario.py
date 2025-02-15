class Usuario:
    """
    Classe que representa um usuário.
    
    Atributos:
        nome (str): Nome do usuário.
        senha (str): Senha do usuário.
    """
    nome: str = ""
    senha: str = ""
    
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha
