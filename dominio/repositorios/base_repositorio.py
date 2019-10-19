"""
Clase Abstracta Repositorio - Define la interfaz más elementla
"""
from abc import *


class BaseRepositorio(metaclass=ABCMeta):

    @property
    def contexto(self):
        return self._contexto

    def __init__(self, contexto):
        self._contexto = contexto
        return

    @abstractmethod
    def agregar(self, entidad):
        pass

    @abstractmethod
    def actualizar(self, entidad):
        pass

    @abstractmethod
    def recuperar(self, id):
        pass

    @abstractmethod
    def obtener_todo(self):
        pass
