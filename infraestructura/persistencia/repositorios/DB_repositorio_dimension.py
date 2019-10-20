from dominio.repositorios.base_repositorio_dimension import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *
import uuid


class DBRepositorioDimension(BaseRepositorioDimension):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, dimension):
        try:
            sesion = self.contexto.sesion
            d = self._mapeador.objeto_valor_a_dto(dimension)
            d.id = str(uuid.uuid4())
            sesion.add(d)
        except Exception("Error al guardar"):
            print("Repositorio de Dimension")
        return

    def actualizar(self, dimension):
        raise ("Metodo no implementado")

    def recuperar(self, dimension):
        try:
            sesion = self.contexto.sesion
            dimension_dto = sesion.query(DimensionElementoDTO).filter_by(tipo_dimension=dimension.tipo_dimension,
                                                                         valor_dimension=dimension.valor_dimension)[0]
            dimension_recuperada = self._mapeador.dto_a_objeto_valor(dimension_dto)
        except Exception("Error al recuperar"):
            dimension_recuperada = None
            print("Repositorio de Elemento")
        return dimension_recuperada

    def eliminar(self, dimension):
        try:
            sesion = self.contexto.sesion
            sesion.delete(sesion.query(DimensionElementoDTO).filter_by(tipo_dimension=dimension.tipo_dimension,
                                                                       valor_dimension=dimension.valor_dimension,
                                                                       id_elemento=dimension.identificacion_elemento)[0])
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento")
        return

    def validar_existencia(self, dimension):
        try:
            sesion = self.contexto.sesion
            dimension_dto = sesion.query(ElementoDTO).filter_by(tipo_dimension=dimension.tipo_dimension,
                                                                valor_dimension=dimension.valor_dimension,
                                                                id_elemento=dimension.id_elemento)[0]
            if dimension_dto is  None:
                return False
            else:
                return True

        except Exception("Error al recuperar"):
            print("Repositorio de Dimension")
        return False

    def recuperar_por_tipo(self, tipo):
        raise ("Metodo no implementado")
        pass

    def recuperar_por_elemento(self, elemento):
        lista_dimensiones = []
        try:
            sesion = self.contexto.sesion
            for dimension_dto in  sesion.query(DimensionElementoDTO).filter_by(id_elemento=elemento):
                dimension = self._mapeador.dto_a_objeto_valor(dimension_dto)
                lista_dimensiones.append(dimension)
            return lista_dimensiones
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento - Dimension")
        return None

    def obtener_todo(self):
        raise (')Metodo no implementado')
        pass
