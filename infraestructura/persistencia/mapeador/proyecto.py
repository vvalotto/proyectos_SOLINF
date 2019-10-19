"""

"""
from sqlalchemy import MetaData

from dominio.entidades.proyecto import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosProyecto:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre = NombreProyecto(self._dto_base_datos.nombre_proyecto)
        tipo_proyecto = self._dto_base_datos.tipo_proyecto
        descripcion = self._dto_base_datos.descripcion
        fecha_fin = self._dto_base_datos.fecha_fin
        self._entidad = Proyecto(nombre, tipo_proyecto, descripcion, fecha_fin)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, proyecto):
        self._entidad = proyecto
        self._dto_base_datos = ProyectoDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = proyecto.identificacion
        self._dto_base_datos.tipo_proyecto = proyecto.tipo_proyecto
        self._dto_base_datos.nombre_proyecto = str(proyecto.nombre)
        self._dto_base_datos.fecha_fin = proyecto.fecha_fin
        self._dto_base_datos.descripcion = proyecto.descripcion
        return self._dto_base_datos
