"""
Entidad Proyecto
"""

from ..base.entidad import *
from ..base.texto_no_vacio import *


TIPO_PROYECTO = ['DESARROLLO', 'MEJORA', 'CORRECTIVO' ]


class NombreProyecto(TextoNoVacio):

    def __repr__(self):
        return self.texto


class DescripcionProyecto(TextoNoVacio):

    def __repr__(self):
        return self.texto


class Proyecto(Entidad):

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        return

    @property
    def tipo_proyecto(self):
        return self._tipo_proyecto

    @tipo_proyecto.setter
    def tipo_proyecto(self, valor):
        if valor in TIPO_PROYECTO:
            self._tipo_proyecto = valor
        else:
            raise Exception("No es un tipo de proyecto valido")
        return

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha_fin(self):
        return self._fecha_fin

    def __init__(self,  nombre, tipo_proyecto, descripcion, fecha_fin):
        super().__init__()
        self._nombre = nombre
        if tipo_proyecto in TIPO_PROYECTO:
            self._tipo_proyecto = tipo_proyecto
        else:
            raise Exception("No es un tipo de proyecto valido")
        self._descripcion = descripcion
        self._fecha_fin = fecha_fin
        return

    def __repr__(self):
        return str(self.nombre) + ": " + self._tipo_proyecto + "\n" + str(self.descripcion)
