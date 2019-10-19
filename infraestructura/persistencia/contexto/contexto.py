"""
Clase Abstracta Contexto para uso de repositorios
"""
from abc import ABCMeta, abstractmethod


class BaseContexto(metaclass=ABCMeta):
    """
    Clase abstracta que define la interfaz de la persistencia de datos
    """
    @abstractmethod
    def __init__(self, recurso):
        """
        Se crea el contexto, donde se pasa el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico
        :param recurso: definicion del recurso fisico
        :return:
        """
        self._recurso = None
        if recurso is None or recurso == "":
            raise Exception("Nombre de recurso vacio")
        self._recurso = recurso
        self._sesion = None
        return

    @property
    def recurso(self):
        return self._recurso

    @property
    def sesion(self):
        return self._sesion

    @sesion.setter
    def sesion(self, valor):
        self._sesion = valor
        return
