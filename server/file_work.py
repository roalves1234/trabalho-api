from time import sleep
from utils import File_Tool

class File_Work:
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
