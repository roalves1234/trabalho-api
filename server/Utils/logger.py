import logging

class Logger:
    """
    Classe para gerenciamento de logs.
    
    Métodos:
        get_instance() -> Logger: Retorna a instância única da classe Logger.
        set(mensagem: str): Registra uma mensagem de log.
        ativar(): Ativa o logger.
        desativar(): Desativa o logger.
    """
    _instance: 'Logger' = None
    _ativo: bool = True
    _logger: logging.Logger = None
    
    @staticmethod
    def get_instance() -> 'Logger':
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        self._ativo = True
        self._logger = self.__get_logger()
    
    def __get_logger(self) -> logging.Logger:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler()
                #logging.FileHandler('api.log')
            ]
        )
        logging.getLogger("uvicorn").propagate = False
        logging.getLogger("uvicorn.access").propagate = False
        logging.getLogger("fastapi").propagate = False

        return logging.getLogger(__name__)
            
    def set(self, mensagem: str):
        if self._ativo:
            self._logger.info(mensagem)
            
    def ativar(self):
        self._ativo = True
        
    def desativar(self):
        self._ativo = False