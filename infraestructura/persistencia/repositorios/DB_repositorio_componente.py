"""
Se implementa el repositorio de la Unidad Academica en Base de Datos
"""
from dominio.repositorios.base_repositorio_componente import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *


class DBRepositorioComponente(BaseRepositorioComponente):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, componente):
        try:
            sesion = self.contexto.sesion
            c = self._mapeador.entidad_a_dto(componente)
            sesion.add(c)
        except Exception("Error al guardar"):
            print("Repositorio de Componente")
        return

    def actualizar(self, componente):
        """
        Para actualizar la entidad persistida, se pasa la entidad modificada y:
            se mapea la entidad a la estructura de tabla
            se recupera la entidad existente por el id
            se copia la estructura mapeada a la recuperada
            se comitea
        :param componente:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            componente_modificado = self._mapeador.entidad_a_dto(componente)
            componente_recuperado = sesion.query(ComponenteDTO).get(componente.identificacion)
            self._copiar_registro(componente_modificado, componente_recuperado)
        except Exception("Error al actualizar"):
            print("Repositorio de Componente")
        return

    def recuperar(self, identificacion):
        try:
            sesion = self.contexto.sesion
            componente_dto = sesion.query(ComponenteDTO).get(identificacion)
            componente = self._mapeador.dto_a_entidad(componente_dto)
        except Exception("Error al recuperar"):
            componente = None
            print("Repositorio de Unidad Academica")
        return componente

    def recuperar_por_nombre(self, nombre):
        try:
            sesion = self.contexto.sesion
            componente_dto = sesion.query(ComponenteDTO).\
                filter(ComponenteDTO.nombre_componente == nombre)[0]
            carrera = self._mapeador.dto_a_entidad(componente_dto)
        except Exception("Error al recuperar"):
            carrera = None
            print("Repositorio de Unidad Academica")
        return carrera

    def validar_existencia(self, nombre):
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(ComponenteDTO).
                        filter(ComponenteDTO.nombre_componente == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Componente")
            return False

    def obtener_todo(self):
        try:
            lista_componentes = []
            sesion = self.contexto.sesion
            for componente_dto in sesion.query(ComponenteDTO).all():
                componente = self._mapeador.dto_a_entidad(componente_dto)
                lista_componentes.append(componente)
            return lista_componentes
        except Exception("Error al recuperar"):
            print("Repositorio de Componente")
            return None

    def obtener_por_proyecto(self, proyecto):
        try:
            lista_componentes = []
            sesion = self.contexto.sesion
            for componente_dto in sesion.query(ComponenteDTO).filter_by(id_proyecto = proyecto):
                componente = self._mapeador.dto_a_entidad(componente_dto)
                lista_componentes.append(componente)
            return lista_componentes
        except Exception("Error al recuperar"):
            print("Repositorio de Componente")
            return None

    @staticmethod
    def _copiar_registro(desde, hacia):
        hacia.nombre_componente = desde.nombre_componente
        hacia.tipo_componente = desde.tipo_componente
        return
