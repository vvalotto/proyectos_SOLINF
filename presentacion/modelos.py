from presentacion.configurador import *


class ListaProyectoVM:

    def __init__(self, gestor):
        self._gestor = gestor
        self._proyectos = []
        return

    def obtener_proyectos(self):
        return self._gestor.obtener_todos_los_proyectos()


class ProyectoVM:

    @property
    def identificador(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def tipo(self):
        return self._tipo

    @property
    def fecha_fin(self):
        return self._fecha_fin

    @property
    def lista(self):
        return self._modulos

    def __init__(self, gestor):
        self._gestor = gestor
        self._id = None
        self._nombre = None
        self._descripcion = None
        self._tipo = None
        self._fecha_fin = None
        self._modulos = []
        return

    def agregar_proyecto(self, nombre_proyecto, tipo_proyecto, descripcion, fecha_fin):
        self._gestor.crear_proyecto(nombre_proyecto, tipo_proyecto, descripcion, fecha_fin)
        self._gestor.guardar_proyecto()
        return

    def existe_proyecto(self, nombre):

       if self._gestor.existe_proyecto(nombre):
           return True
       else:
           return False

    def recuperar_proyecto(self, id):
        try:
            proyecto = self._gestor.recuperar_proyecto(id)
            self._id = proyecto.identificacion
            self._nombre = proyecto.nombre
            self._descripcion = proyecto.descripcion
            self._tipo = proyecto.tipo_proyecto
            self._fecha_fin = proyecto.fecha_fin

        except Exception:
            return None
        return True

    def obtener_proyecto(self, nombre):
        proyecto = self._gestor.recuperar_proyecto_por_nombre(nombre)
        self._id = proyecto.identificacion
        self._nombre = nombre
        self._descripcion = proyecto.descripcion
        self._tipo = proyecto.tipo_proyecto
        self._fecha_fin = proyecto.fecha_fin
        return

    def listar_modulos(self):
        self._modulos = []
        repo_componente = DBRepositorioComponente(Configurador.contexto, MapeadorDatosComponente(Configurador.contexto))
        gestor_componente = GestorComponente()
        gestor_componente.asignar_repositorio(repo_componente)
        lista_componentes = gestor_componente.obtener_componentes_del_proyecto(self._id)
        for componente in lista_componentes:
            self._modulos.append(componente)
        return
