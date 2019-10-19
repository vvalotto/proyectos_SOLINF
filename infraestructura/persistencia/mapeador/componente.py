"""

"""
from sqlalchemy import MetaData

from dominio.entidades.componente import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosComponente:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre_componente = NombreComponente(self._dto_base_datos.nombre_componente)
        tipo_componente = self._dto_base_datos.tipo_componente
        id_proyecto = self._dto_base_datos.id_proyecto
        self._entidad = Componente(nombre_componente, tipo_componente, id_proyecto)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, componente):
        self._entidad = componente
        self._dto_base_datos = ComponenteDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = componente.identificacion
        self._dto_base_datos.tipo_componente = componente.tipo_componente
        self._dto_base_datos.nombre_componente = str(componente.nombre)
        self._dto_base_datos.id_proyecto = componente.identificacion_proyecto
        return self._dto_base_datos
