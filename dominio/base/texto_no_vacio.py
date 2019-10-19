"""
Objeto Valor con texto que valida que no este vacio
"""

from .objeto_valor import *
from .validador import *


class TextoNoVacio(ObjetoValor):

    @property
    def texto(self):
        return self._texto

    def __init__(self, texto):

        validacion = ValidadorTexto().validar(texto)

        if not validacion.valido:
            raise Exception(validacion.resultado)
        else:
            self._texto = texto
        return

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._texto]

    def __str__(self):
        return self._texto


class ValidadorTextoNoVacio(BaseValidador):
    def validar(self, texto):
        if texto == "":
            self._valido = False
            self._resultado = "Error: Esta Vacio"
        return self


class ValidadorTextoNoNulo(BaseValidador):
    def validar(self, texto):
        if texto is None:
            self._valido = False
            self._resultado = "Error: EsNulo"
        return self


class ValidadorTexto(BaseValidador):
    def validar(self, texto):
        validacion = ValidadorTextoNoVacio().validar(texto)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        validacion = ValidadorTextoNoNulo().validar(texto)
        self._valido = self._valido and validacion.valido
        self._resultado = self._resultado + validacion.resultado

        return self
