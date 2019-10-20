"""
Servicio de Aplicacion que gestiona el tratamiento de los elementos o partes que constituyen el
componente se software a construir
"""
from sqlalchemy.orm import sessionmaker
from dominio.entidades.elemento import *
from infraestructura.persistencia.repositorios.DB_repositorio_elemento import *
from infraestructura.persistencia.mapeador.elemento import *


class GestorElemento:
    """
    Clase de aplicación que es la responsable de realizar la
    administración de agregado Elemento compuesto de la entidad
    Elemento
    """
    def __init__(self):
        self._elemento = None
        self._repositorio = None
        self._nuevo = False
        return

    def crear_elemento(self, nombre_elemento,
                             tipo_elemento,
                             descripcion,
                             id_componente):
        """
        Metodo Factoria que crea solo una nueva entidad elemento
        :return: la proyecto creado
        """
        self._elemento = Elemento(nombre_elemento, tipo_elemento, descripcion, id_componente)
        self._nuevo = True
        return self._elemento

    def asignar_repositorio(self, repositorio):
        """
        Asocia el repositorio donde se persisten las entidades
        :param repositorio:
        :return:
        """
        self._repositorio = repositorio
        return

    def guardar_elemento(self):
        """
        Persiste los cambios en el agregado:
        Ya sea un elemento nuevo, se modifica los datos del elemento
        o se cambian los OV
        :return:
        """
        self._abrir_unidad_de_trabajo()
        if self._nuevo:
            try:
                if not self.existe_elemento(str(self._elemento.nombre_elemento)):
                    self._repositorio.agregar(self._elemento)
                else:
                    raise("Ya existe es elemento con el nombre:" + str(self._elemento.nombre_elemento))
            except Exception():
                print('Error al guardar')
        else:
            try:
                self._repositorio.actualizar(self._elemento)
            except Exception():
                print('Error al guardar')
        self._nuevo = False

        self._cerrar_unidad_de_trabajo()
        return

    def recuperar_elemento_por_nombre(self, nombre):
        self._abrir_unidad_de_trabajo()
        self._elemento = self._repositorio.recuperar_por_nombre(nombre)
        for dim in self._repositorio.recuperar_dimensiones(self._elemento.identificacion):
            self._elemento.recuperar_dimension(dim)
        for esf in self._repositorio.recuperar_esfuerzos(self._elemento.identificacion):
            self._elemento.recuperar_esfuerzo(esf)
        for dfc in self._repositorio.recuperar_defectos(self._elemento.identificacion):
            self._elemento.recuperar_defecto(dfc)
        self._cerrar_unidad_de_trabajo()
        return self._elemento

    def recuperar_elemento(self, id_elemento):
        self._abrir_unidad_de_trabajo()
        self._elemento = self._repositorio.recuperar(id_elemento)
        for dim in self._repositorio.recuperar_dimensiones(self._elemento.identificacion):
            self._elemento.recuperar_dimension(dim)
        for esf in self._repositorio.recuperar_esfuerzos(self._elemento.identificacion):
            self._elemento.recuperar_esfuerzo(esf)
        for dfc in self._repositorio.recuperar_defectos(self._elemento.identificacion):
            self._elemento.recuperar_defecto(dfc)
        self._cerrar_unidad_de_trabajo()
        return self._elemento

    def obtener_elementos_del_proyecto(self, proyecto):
        self._abrir_unidad_de_trabajo()
        lista_elementos = self._repositorio.obtener_por_proyecto(proyecto)
        self._cerrar_unidad_de_trabajo()
        return lista_elementos

    def obtener_elementos_del_componente(self, componente):
        self._abrir_unidad_de_trabajo()
        lista_elementos = self._repositorio.obtener_por_componente(componente)
        self._cerrar_unidad_de_trabajo()
        return lista_elementos

    def existe_elemento(self, nombre):
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
