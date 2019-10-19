"""
Servicio de Aplicacion que gestiona el tratamiento de las unidades academicas
"""
from sqlalchemy.orm import sessionmaker
from dominio.entidades.proyecto import *


class GestorProyecto:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de la entidad Proyecto.
    Basicamente maneja los CRUD de la entidad, no tiene otra
    responsabilidad
    """
    def __init__(self):
        self._proyecto = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_proyecto(self, nombre_proyecto,
                             tipo_proyecto,
                             descripcion,
                             fecha_fin):
        """
        Metodo Factoria que crea una nueva entidad
        :param nombre_proyecto:  (OV)
        :param tipo_proyecto:
        :param descripcion:
        :param fecha_fin
        :return: la proyecto creado
        """
        self._proyecto = Proyecto(nombre_proyecto,
                                  tipo_proyecto,
                                  descripcion,
                                  fecha_fin)
        self._nuevo = True
        return self._proyecto

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_proyecto(self):
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                self._repositorio.agregar(self._proyecto)
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._proyecto)
            except Exception():
                print('Error al guardar')
        self._cerrar_unidad_de_trabajo()
        self._nuevo = False
        return

    def recuperar_proyecto_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._proyecto = self._repositorio.recuperar_por_nombre(nombre)
        self._cerrar_unidad_de_trabajo()
        return self._proyecto

    def recuperar_proyecto(self, id_proyecto):
        self._abrir_unidad_de_trabajo()
        """
        dto = self._repositorio.recuperar(id_proyecto)
        self._proyecto = self._mapear_DTO_a_proyecto(dto)
        """
        self._proyecto = self._repositorio.recuperar(id_proyecto)
        self._cerrar_unidad_de_trabajo()
        return self._proyecto

    def obtener_todos_los_proyectos(self):
        self._abrir_unidad_de_trabajo()
        lista_proyectos = self._repositorio.obtener_todo()
        """
        for ua in list(self._repositorio.obtener_todo()):
            lista_unidad_academica.append(self._mapear_DTO_a_unidad_academica(ua))
        """
        self._cerrar_unidad_de_trabajo()
        return lista_proyectos

    def existe_proyecto(self, nombre):
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
