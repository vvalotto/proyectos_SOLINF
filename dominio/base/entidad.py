"""
Clase Base Entidad
"""

from abc import ABCMeta
import uuid


class Entidad(metaclass=ABCMeta):

    @property
    def identificacion(self):
        return self._id

    @identificacion.setter
    def identificacion(self, valor):
        self._id = valor
        return

    def __init__(self):
        self._id = str(uuid.uuid4())
        return

    def __eq__(self, otra_entidad):
        """
        Compara si dos entidades son las mismas
        :param otra_entidad: entidad a comparar
        :return:
        """
        if otra_entidad.id is None:
            raise EntidadSinIdentificacion()
        return self._id == otra_entidad.id


class EntidadSinIdentificacion(Exception):

    def __init__(self):
        print("Error: Entidad Sin Identificacion")
        return
