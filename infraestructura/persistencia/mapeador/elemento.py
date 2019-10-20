"""

"""
from sqlalchemy import MetaData

from dominio.entidades.elemento import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class MapeadorDatosElemento:

    def __init__(self, contexto):
        self._contexto = contexto
        self._entidad = None
        self._dto_base_datos = None
        return

    def dto_a_entidad(self, dto):
        self._dto_base_datos = dto
        nombre_elemento = NombreElemento(self._dto_base_datos.nombre_elemento)
        tipo_elemento = self._dto_base_datos.tipo_elemento
        descripcion = self._dto_base_datos.descripcion
        id_componente = self._dto_base_datos.id_componente
        self._entidad = Elemento(nombre_elemento, tipo_elemento, descripcion, id_componente)
        self._entidad.identificacion = self._dto_base_datos.id
        return self._entidad

    def entidad_a_dto(self, elemento):
        self._entidad = elemento
        self._dto_base_datos = ElementoDTO()
        self._dto_base_datos.metadata = MetaData(bind=self._contexto.recurso)
        self._dto_base_datos.id = elemento.identificacion
        self._dto_base_datos.tipo_elemento = elemento.tipo_elemento
        self._dto_base_datos.nombre_elemento = str(elemento.nombre_elemento)
        self._dto_base_datos.descripcion = elemento.descripcion
        self._dto_base_datos.id_componente = elemento.id_componente
        return self._dto_base_datos
