import configparser
import os
from abc import ABC


class BaseConfig(ABC):
    FILE_NAME = ''

    _config = list()

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(self._determine_config_file_path())

    def _determine_config_file_path(self) -> str | bytes:
        return os.path.join(os.path.dirname(__file__), self.FILE_NAME)

    def get_config(self) -> dict:
        return self._config
