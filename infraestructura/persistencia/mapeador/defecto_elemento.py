"""

"""
from sqlalchemy import MetaData

from dominio.entidades.elemento import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosDefecto:

    def __init__(self, contexto):
        self._contexto = contexto
        self._objeto_valor = None
        self._dto_base_datos = None
        return

    def dto_a_objeto_valor(self, dto):
        self._dto_base_datos = dto
        fase_defecto = self._dto_base_datos.fase_defecto
        cantidad_defecto = self._dto_base_datos.cantidad_defecto
        id_elemento = self._dto_base_datos.id_elemento
        self._objeto_valor = Defecto(fase_defecto, cantidad_defecto, id_elemento)
        return self._objeto_valor

    def objeto_valor_a_dto(self, defecto):
        self._objeto_valor = defecto
        self._dto_base_datos = DefectoElementoDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.fase_defecto = str(defecto.fase_defecto)
        self._dto_base_datos.cantidad_defecto = defecto.cantidad_defecto
        self._dto_base_datos.id_elemento = defecto.identificacion_elemento
        return self._dto_base_datos
