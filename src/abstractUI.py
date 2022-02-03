from .FileCopyDeleter import FileCopyDeleter
from .config import Config

class AbstractUI:
    def __init__(self, config_obj: Config) -> None:
        self._config = config_obj
        self._deleter = FileCopyDeleter()
        self._deleter.path = self._config.path
        self._deleter.types = self._config.types