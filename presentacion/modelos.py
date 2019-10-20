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


class ListaComponenteVM:

    def __init__(self, gestor):
        self._gestor = gestor
        self._componentes= []
        return

    def obtener_componentes(self):
        return self._gestor.obtener_todos_los_componentes()


class ComponenteVM:

    @property
    def nombre(self):
        return self._nombre_componente

    @property
    def tipo(self):
        return self._tipo_componente

    @property
    def identificador(self):
        return self._id

    @property
    def lista_elementos(self):
        return self._elementos

    @property
    def proyecto(self):
        return self._proyecto

    def __init__(self, gestor):
        self._gestor = gestor
        self._nombre_componente= None
        self._tipo_componente = None
        self._id = None
        self._id_proyecto = None
        self._proyecto = None
        self._elementos = []
        return

    def existe_componente(self, nombre):
        if self._gestor.recuperar_componente(nombre):
            return True
        else:
            return False

    def recuperar_componente(self, id):
        try:
            componente = self._gestor.recuperar_componente(id)
            self._id = componente.identificacion
            self._nombre_componente = componente.nombre
            self._tipo_componente = componente.tipo_componente
            self._id_proyecto = componente.identificacion_proyecto
            self._proyecto = Configurador.gestor_proyecto.recuperar_proyecto(self._id_proyecto).nombre
        except Exception:
            return None
        return componente

    def listar_elementos(self):
        self._elementos = []
        repo_elemento = DBRepositorioElemento(Configurador.contexto, MapeadorDatosElemento(Configurador.contexto))
        gestor_elemento= GestorElemento()
        gestor_elemento.asignar_repositorio(repo_elemento)
        lista_componentes = gestor_elemento.obtener_elementos_del_componente(self._id)
        for componente in lista_componentes:
            self._elementos.append(componente)
        return


class ListaElementosVM:

    def __init__(self, gestor):
        self._gestor = gestor
        self._elementos = []
        return

    def obtener_elementos(self):
        return self._gestor.obtener_todos_los_elementos()


class ElementoVM:

    @property
    def nombre_elemento(self):
        return self._nombre_elemento

    @property
    def tipo_elemento(self):
        return self._tipo_elemento

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def identificador(self):
        return self._id

    @property
    def dimensiones(self):
        return self._dimensiones

    @property
    def esfuerzos(self):
        return self._esfuerzos

    @property
    def defectos(self):
        return self._defectos

    @property
    def proyecto(self):
        return self._proyecto

    @property
    def componente(self):
        return self._componente

    def __init__(self, gestor):
        self._gestor = gestor
        self._nombre_elemento = None
        self._tipo_elemento = None
        self._descripcion = None
        self._id = None
        self._id_componente = None
        self._dimensiones = []
        self._esfuerzos = []
        self._defectos = []
        self._proyecto = None
        self._componente = None
        return

    def existe_elemento(self, id):
        if self._gestor.existe_componente(id):
            return True
        else:
            return False

    def recuperar_elemento(self, id):
        elemento = self._gestor.recuperar_elemento(id)
        self._id = elemento.identificacion
        self._nombre_elemento = elemento.nombre_elemento
        self._tipo_elemento = elemento.tipo_elemento
        self._id_componente = elemento.id_componente
        self._descripcion = elemento.descripcion

        componente = Configurador.gestor_componente.recuperar_componente(elemento._id_componente)
        self._componente = componente.nombre

        proyecto = Configurador.gestor_proyecto.recuperar_proyecto(componente._id_proyecto)
        self._proyecto = proyecto.nombre

        self._dimensiones = elemento.lista_dimensiones
        self._esfuerzos = elemento.lista_esfuerzos
        self._defectos = elemento.lista_defectos
        return elemento
