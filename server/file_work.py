from time import sleep
from Utils.utils import File_Tool

class File_Work:
    """
    Classe para manipulação de trabalhos com arquivos.
    
    Atributos:
        file (File_Tool): Instância da classe File_Tool para manipulação de arquivos.
        texto (str): Texto a ser salvo no arquivo.
    
    Métodos:
        do_tempo(texto: str): Salva o texto no arquivo com um efeito de tempo.
        do_texto(texto: str): Define o texto e chama o método do_tempo.
        do_completando(completando: str): Salva o texto completado no arquivo.
    """
    def __init__(self):
        self.file: File_Tool = File_Tool("output.md")
        self.texto: str = ""
    
    def do_tempo(self, texto: str):
        self.file.save(f"# {texto}")
        sleep(0.4)
        self.file.save(f"# {texto}.")
        sleep(0.4)
        self.file.save(f"# {texto}..")
        sleep(0.4)
        self.file.save(f"# {texto}...")

    def do_texto(self, texto: str):
        self.texto = texto
        self.do_tempo(texto.strip())
        
    def do_completando(self, completando: str):
        self.file.save(f"# {self.texto}*{completando}*")
