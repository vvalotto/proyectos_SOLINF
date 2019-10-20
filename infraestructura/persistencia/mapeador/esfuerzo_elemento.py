"""

"""
from sqlalchemy import MetaData

from dominio.entidades.elemento import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosEsfuerzo:

    def __init__(self, contexto):
        self._contexto = contexto
        self._objeto_valor = None
        self._dto_base_datos = None
        return

    def dto_a_objeto_valor(self, dto):
        self._dto_base_datos = dto
        tipo_actividad = self._dto_base_datos.tipo_actividad
        esfuerzo_actividad = self._dto_base_datos.esfuerzo_actividad
        id_elemento = self._dto_base_datos.id_elemento
        self._objeto_valor = Esfuerzo(tipo_actividad, esfuerzo_actividad, id_elemento)
        return self._objeto_valor

    def objeto_valor_a_dto(self, esfuerzo):
        self._objeto_valor = esfuerzo
        self._dto_base_datos = EsfuerzoElementoDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.tipo_actividad = str(esfuerzo.tipo_actividad)
        self._dto_base_datos.esfuerzo_actividad = esfuerzo.esfuerzo_actividad
        self._dto_base_datos.id_elemento = esfuerzo.identificacion_elemento
        return self._dto_base_datos
