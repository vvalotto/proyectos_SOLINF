"""
Se implementa el repositorio de la Elementos en Base de Datos
"""
from dominio.repositorios.base_repositorio_elemento import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *
from infraestructura.persistencia.mapeador.dimension_elemento import *
from infraestructura.persistencia.mapeador.esfuerzo_elemento import *

from .DB_repositorio_dimension import *
from .DB_repositorio_esfuerzo import *


class DBRepositorioElemento(BaseRepositorioElemento):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        self._repo_dimension = DBRepositorioDimension(contexto, MapeadorDatosDimension(contexto))
        self._repo_esfuerzo = DBRepositorioEsfuerzo(contexto, MapeadorDatosEsfuerzo(contexto))
        return

    def agregar(self, elemento):
        """
        Persiste el elemento
        :param elemento:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            c = self._mapeador.entidad_a_dto(elemento)
            sesion.add(c)
        except Exception("Error al guardar"):
            print("Repositorio de Elemento")
        return

    def actualizar(self, elemento):
        """
        Para actualizar la entidad persistida, se pasa la entidad modificada y:
            se mapea la entidad a la estructura de tabla
            se recupera la entidad existente por el id
            se copia la estructura mapeada a la recuperada
            se comitea
        :param elemento:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            elemento_modificado = self._mapeador.entidad_a_dto(elemento)
            elemento_recuperado = sesion.query(ElementoDTO).get(elemento.identificacion)
            self._copiar_registro(elemento_modificado, elemento_recuperado)
        except Exception("Error al actualizar"):
            print("Repositorio de elemento")
        return

    def recuperar(self, identificacion):
        """
        Recupera el elemento por el id de la entidad desde la
        persistencia
        :param identificacion: id de la entidad elemento
        :return:
        """
        try:
            sesion = self.contexto.sesion
            elemento_dto = sesion.query(ElementoDTO).get(identificacion)
            elemento = self._mapeador.dto_a_entidad(elemento_dto)
        except Exception("Error al recuperar"):
            elemento = None
            print("Repositorio de Elemento")
        return elemento

    def recuperar_por_nombre(self, nombre):
        """
        Recupera el elemento que se consultado por el nombre
        :param nombre:
        :return:
        """
        try:
            sesion = self.contexto.sesion
            elemento_dto = sesion.query(ElementoDTO).\
                filter(ElementoDTO.nombre_elemento == nombre)[0]
            elemento = self._mapeador.dto_a_entidad(elemento_dto)
        except Exception("Error al recuperar"):
            elemento = None
            print("Repositorio de Elemento")
        return elemento

    def validar_existencia(self, nombre):
        """
        Consulta si ya existe el elemento identificado por el nombre
        Es para no repetir nombres
        """
        try:
            sesion = self.contexto.sesion
            if len(list(sesion.query(ElementoDTO).
                        filter(ElementoDTO.nombre_elemento == nombre))) > 0:
                return True
            else:
                return False
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return False

    def obtener_todo(self):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for elemento_dto in sesion.query(ElementoDTO).all():
                elemento = self._mapeador.dto_a_entidad(elemento_dto)
                lista_elementos.append(elemento)
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def obtener_por_proyecto(self, proyecto):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for componente_dto in sesion.query(ComponenteDTO).filter_by(id_proyecto=proyecto):
                lista_elementos.append(self.obtener_por_componente(componente_dto.id))
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def obtener_por_componente(self, componente):
        try:
            lista_elementos = []
            sesion = self.contexto.sesion
            for elemento_dto in sesion.query(ElementoDTO).filter_by(id_componente=componente):
                elemento = self._mapeador.dto_a_entidad(elemento_dto)
                lista_elementos.append(elemento)
            return lista_elementos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
            return None

    def agregar_dimension_elemento(self, dimension_elemento):
        """
        Persiste un nueva dimension para elemento.
        :param dimension_elemento:
        """
        self._repo_dimension.agregar(dimension_elemento)
        return

    def eliminar_dimension_elemento(self, dimension_elemento):
        self._repo_dimension.eliminar(dimension_elemento)
        return

    def recuperar_dimension_elemento(self, dimension_elemento):
        return self._repo_dimension.recuperar(dimension_elemento)

    def validar_existencia_dimension_elemento(self, dimension_elemento):
        encontro = False
        return encontro

    def recuperar_dimensiones(self, elemento):
        return self._repo_dimension.recuperar_por_elemento(elemento)

    def agregar_esfuerzo_elemento(self, esfuerzo_elemento):
        """
        Persiste un nueva dimension para elemento.
        :param esfuerzo_elemento:
        """
        self._repo_esfuerzo.agregar(esfuerzo_elemento)
        return

    def eliminar_esfuerzo_elemento(self, esfuerzo_elemento):
        self._repo_esfuerzo.eliminar(esfuerzo_elemento)
        return

    def recuperar_esfuerzo_elemento(self, esfuerzo_elemento):
        return self._repo_esfuerzo.recuperar(esfuerzo_elemento)

    def validar_existencia_efuerzo_elemento(self, efuerzo_elemento):
        encontro = False
        return encontro

    def recuperar_esfuerzos(self, elemento):
        return self._repo_esfuerzo.recuperar_por_elemento(elemento)

    @staticmethod
    def _copiar_registro(desde, hacia):
        hacia.nombre_elemento = desde.nombre_elemento
        hacia.tipo_elemento = desde.tipo_elemento
        hacia.descripcio = desde.descripcion
        return
