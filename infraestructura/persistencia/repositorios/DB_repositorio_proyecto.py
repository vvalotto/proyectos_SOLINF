"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from dominio.repositorios.base_repositorio_proyecto import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class DBRepositorioProyecto(BaseRepositorioProyecto):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, proyecto):
        try:
            sesion = self.contexto.sesion
            sesion.add(self._mapeador.entidad_a_dto(proyecto))
        except Exception("Error al guardar"):
            print("Repositorio de proyecto")
        return

    def actualizar(self, proyecto):
        """
        Para actualizar la entidad persistida, se pasa la entidad modificada y:
            se mapea la entidad a la estructura de tabla
            se recupera la entidad existente por el id
            se copia la estructura mapeada a la recuperada
            se comitea
        :param proyecto:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            proyecto_modificado = self._mapeador.entidad_a_dto(proyecto)
            proyecto_recuperado = sesion.query(ProyectoDTO).get(proyecto.identificacion)
            self._copiar_registro(proyecto_modificado, proyecto_recuperado)
        except Exception("Error al actualizar"):
            print("Repositorio de Proyecto")
        return

    def recuperar(self, identificacion):
        try:
            sesion = self.contexto.sesion
            proyecto_dto = sesion.query(ProyectoDTO).get(identificacion)
            proyecto = self._mapeador.dto_a_entidad(proyecto_dto)
        except Exception("Error al recuperar"):
            proyecto = None
            print("Repositorio de Proyecto")
        return proyecto

    def recuperar_por_nombre(self, nombre):
        try:
            sesion = self.contexto.sesion
            proyecto_dto = sesion.query(ProyectoDTO).\
                           filter(ProyectoDTO.nombre_proyecto == nombre)[0]
            proyecto = self._mapeador.dto_a_entidad(proyecto_dto)
        except Exception("Error al recuperar"):
            proyecto = None
            print("Repositorio de Unidad Academica")
        return proyecto

    def validar_existencia(self, nombre):
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(ProyectoDTO).
                            filter(ProyectoDTO.nombre_proyecto == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Proyecto")
            return False

    def obtener_todo(self):
        try:
            lista_proyectos = []
            sesion = self.contexto.sesion
            for proyecto_dto in sesion.query(ProyectoDTO).all():
                proyecto = self._mapeador.dto_a_entidad(proyecto_dto)
                lista_proyectos.append(proyecto)
            return lista_proyectos
        except Exception("Error al recuperar"):
            print("Repositorio de Proyecto")
            return None

    @staticmethod
    def _copiar_registro(desde, hacia):
        hacia.nombre_proyecto = desde.nombre_proyecto
        hacia.descripcion = desde.descripcion
        hacia.fecha_fin = desde.fecha_fin
        hacia.id_componente = desde.id_componente
        return
