"""
Clase Abstracta que define el repositorio
"""
from .base_repositorio import *


class BaseRepositorioDefecto(BaseRepositorio):

    @abstractmethod
    def eliminar(self, ov):
        pass

    @abstractmethod
    def validar_existencia(self, ov):
        pass

    @abstractmethod
    def recuperar_por_fase(self, tipo):
        pass

    @abstractmethod
    def recuperar_por_elemento(self, elemento):
        pass
