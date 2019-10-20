from dominio.repositorios.base_repositorio_esfuerzo import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import *
import uuid


class DBRepositorioEsfuerzo(BaseRepositorioEsfuerzo):

    def __init__(self, contexto, mapeador):
        super().__init__(contexto)
        self._mapeador = mapeador
        return

    def agregar(self, efuerzo):
        try:
            sesion = self.contexto.sesion
            d = self._mapeador.objeto_valor_a_dto(efuerzo)
            d.id = str(uuid.uuid4())
            sesion.add(d)
        except Exception("Error al guardar"):
            print("Repositorio de Efuerzo")
        return

    def actualizar(self, esfuerzo):
        raise ("Metodo no implementado")
        return

    def recuperar(self, esfuerzo):
        try:
            sesion = self.contexto.sesion
            esfuerzo_dto = sesion.query(EsfuerzoElementoDTO).filter_by(tipo_dimension=esfuerzo.tipo_actividad,
                                                                       valor_dimension=esfuerzo.esfuerzo_actividad)[0]
            esfuerzo_recuperado = self._mapeador.dto_a_objeto_valor(esfuerzo_dto)
        except Exception("Error al recuperar"):
            esfuerzo_recuperado = None
            print("Repositorio de Esfuerzo")
        return esfuerzo_recuperado

    def eliminar(self, esfuerzo):
        try:
            sesion = self.contexto.sesion
            sesion.delete(sesion.query(EsfuerzoElementoDTO).filter_by(tipo_dimension=esfuerzo.tipo_actividad,
                                                                      valor_dimension=esfuerzo.esfuerzo_actividad,
                                                                      id_elemento=esfuerzo.identificacion_elemento)[0])
        except Exception("Error al recuperar"):
            print("Repositorio de Esfuerzo")
        return

    def validar_existencia(self, esfuerzo):
        try:
            sesion = self.contexto.sesion
            esfuerzo_dto = sesion.query(EsfuerzoElementoDTO).filter_by(tipo_dimension=esfuerzo.tipo_actividad,
                                                                       valor_dimension=esfuerzo.esfuerzo_actividad,
                                                                       id_elemento=esfuerzo.id_elemento)[0]
            if esfuerzo_dto is None:
                return False
            else:
                return True

        except Exception("Error al recuperar"):
            print("Repositorio de Esfuerzo")
        return False

    def recuperar_por_actividad(self, actividad):
        raise ("Metodo no implementado")
        pass

    def recuperar_por_elemento(self, elemento):
        lista_esfuerzos = []
        try:
            sesion = self.contexto.sesion
            for esfuerzo_dto in  sesion.query(EsfuerzoElementoDTO).filter_by(id_elemento=elemento):
                esfuerzo = self._mapeador.dto_a_objeto_valor(esfuerzo_dto)
                lista_esfuerzos.append(esfuerzo)
            return lista_esfuerzos
        except Exception("Error al recuperar"):
            print("Repositorio de Elemento - Esfuerzo")
        return None

    def obtener_todo(self):
        raise ("Metodo no implementado")
        pass