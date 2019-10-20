"""

"""
from sqlalchemy import MetaData

from dominio.entidades.elemento import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosDimension:

    def __init__(self, contexto):
        self._contexto = contexto
        self._objeto_valor = None
        self._dto_base_datos = None
        return

    def dto_a_objeto_valor(self, dto):
        self._dto_base_datos = dto
        tipo_dimension = self._dto_base_datos.tipo_dimension
        valor = self._dto_base_datos.valor_dimension
        id_elemento = self._dto_base_datos.id_elemento
        self._objeto_valor = Dimension(tipo_dimension, valor, id_elemento)
        return self._objeto_valor

    def objeto_valor_a_dto(self, dimension):
        self._objeto_valor = dimension
        self._dto_base_datos = DimensionElementoDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.tipo_dimension = str(dimension.tipo_dimension)
        self._dto_base_datos.valor_dimension = dimension.valor_dimension
        self._dto_base_datos.id_elemento = dimension.identificacion_elemento
        return self._dto_base_datos