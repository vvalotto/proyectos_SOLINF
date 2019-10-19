"""
Clase Abstracta que define el repositorio de la Unidad Academica
"""
from .base_repositorio import *


class BaseRepositorioProyecto(BaseRepositorio):

    @abstractmethod
    def validar_existencia(self, criterio):
        pass

    @abstractmethod
    def recuperar_por_nombre(self, nombre):
        pass
