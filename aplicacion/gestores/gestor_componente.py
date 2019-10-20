"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from sqlalchemy.orm import sessionmaker
from dominio.entidades.componente import *


class GestorComponente:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Componente.
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._componente = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_componente(self, nombre_componente, tipo_componente, id_proyecto):
        """
        Metodo Factoria que crea una nueva entidad
        :return: la proyecto creado
        """
        self._componente = Componente(nombre_componente, tipo_componente, id_proyecto)
        self._nuevo = True
        return self._componente

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_componente(self):
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._componente)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._componente)
            except Exception():
                print('Error al guardar')
        self._cerrar_unidad_de_trabajo()
        self._nuevo = False
        return

    def recuperar_componente_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._componente = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._componente

    def recuperar_componente(self, id_componente):
        self._abrir_unidad_de_trabajo()
        self._componente = self._repositorio.recuperar(id_componente)
        self._cerrar_unidad_de_trabajo()
        return self._componente

    def obtener_componentes_del_proyecto(self, proyecto):
        self._abrir_unidad_de_trabajo()
        lista_componentes = self._repositorio.obtener_por_proyecto(proyecto)
        self._cerrar_unidad_de_trabajo()
        return lista_componentes

    def existe_componente(self, nombre):
        self._abrir_unidad_de_trabajo()
        valida = self._repositorio.validar_existencia(nombre)
        self._cerrar_unidad_de_trabajo()
        return valida

    def _abrir_unidad_de_trabajo(self):
        sesion = sessionmaker(bind=self._repositorio.contexto.recurso)
        self._repositorio.contexto.sesion = sesion()
        return

    def _cerrar_unidad_de_trabajo(self):
        self._repositorio.contexto.sesion.commit()
        return
