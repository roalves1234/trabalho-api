import logging

class Logger:
    _instance = None
    _ativo = True
    _logger = None
    
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        self._ativo = True
        self._logger = self.__get_logger()
    
    def __get_logger(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('api.log')
            ]
        )

        return logging.getLogger(__name__)
            
    def set(self, mensagem: str):
        if self._ativo:
            self._logger.info(mensagem)
            
    def ativar(self):
        self._ativo = True
        
    def desativar(self):
        self._ativo = False