from dominio.repositorios.base_repositorio_defecto import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *
import uuid


class DBRepositorioDefecto(BaseRepositorioDefecto):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, defecto):
        try:
            sesion = self.contexto.sesion
            d = self._mapeador.objeto_valor_a_dto(defecto)
            d.id = str(uuid.uuid4())
            sesion.add(d)
        except Exception("Error al guardar"):
            print("Repositorio de Defecto")
        return

    def actualizar(self, defecto):
        raise ("Metodo no implementado")
        return

    def recuperar(self, defecto):
        try:
            sesion = self.contexto.sesion
            defecto_dto = sesion.query(DefectoElementoDTO).filter_by(fase_defecto=defecto.fase_defecto,
                                                                     cantidad_defecto=defecto.cantidad_defecto)[0]
            defecto_recuperado = self._mapeador.dto_a_objeto_valor(defecto_dto)
        except Exception("Error al recuperar"):
            defecto_recuperado = None
            print("Repositorio de Defecto")
        return defecto_recuperado

    def eliminar(self, defecto):
        try:
            sesion = self.contexto.sesion
            sesion.delete(sesion.query(DefectoElementoDTO).filter_by(fase_defecto=defecto.fase_defecto,
                                                                     cantidad_defecto=defecto.cantidad_defecto,
                                                                     id_elemento=defecto.identificacion_elemento)[0])
        except Exception("Error al recuperar"):
            print("Repositorio de Defecto")
        return

    def validar_existencia(self, defecto):
        try:
            sesion = self.contexto.sesion
            defecto_dto = sesion.query(DefectoElementoDTO).filter_by(fase_defecto=defecto.fase_defecto,
                                                                     cantidad_defecto=defecto.cantidad_defecto,
                                                                     id_elemento=defecto.identificacion_elemento)[0]
            if defecto_dto is  None:
                return False
            else:
                return True

        except Exception("Error al recuperar"):
            print("Repositorio de Dimension")
        return False

    def recuperar_por_fase(self, tipo):
        raise ("Metodo no implementado")
        pass

    def recuperar_por_elemento(self, elemento):
        lista_defectos = []
        try:
            sesion = self.contexto.sesion
            for defecto_dto in  sesion.query(DefectoElementoDTO).filter_by(id_elemento=elemento):
                defecto = self._mapeador.dto_a_objeto_valor(defecto_dto)
                lista_defectos.append(defecto)
            return lista_defectos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento - Defecto")
        return None

    def obtener_todo(self):
        raise ("Metodo no implementado")
        pass
