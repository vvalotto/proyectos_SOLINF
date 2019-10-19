"""
Clase Abstracta Validador
"""

from abc import *


class BaseValidador(metaclass=ABCMeta):

    @property
    def valido(self):
        return self._valido

    @property
    def resultado(self):
        return self._resultado

    def __init__(self):
        self._valido = True
        self._resultado = ""
        return

    def validar(self, objeto):
        pass
