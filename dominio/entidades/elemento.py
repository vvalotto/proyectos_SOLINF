"""
Entidad Elemento
"""

from ..base.entidad import *
from ..base.texto_no_vacio import *

TIPO_ELEMENTO = ['Caso de Uso', 'Historia de Usuario', 'Escenario de Calidad', "Requerimiento", "POC"]
TIPO_ACTIVIDAD = ['Análisis', 'Diseño', 'Programación', 'Testing', 'Retrabajo', 'Revisión']
FASE_DEFECTO = ['CASOS_DE_PRUEBA', 'TEST_FUNCIONAL', 'TEST_USUARIO']


class Dimension(ObjetoValor):

    @property
    def tipo_dimension(self):
        return self._tipo_dimension

    @tipo_dimension.setter
    def tipo_dimension(self, valor):
        self._tipo_dimension = valor
        return

    @property
    def valor_dimension(self):
        return self._valor_dimension

    @valor_dimension.setter
    def valor_dimension(self, valor):
        self._valor_dimension = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self,  tipo_dimension, valor_dimension, elemento):
        self._tipo_dimension = tipo_dimension
        self._valor_dimension = valor_dimension
        self._id_elemento = elemento
        return

    def __repr__(self):
        return self.tipo_dimension + ": " + str(self.valor_dimension)

    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        return [self._tipo_dimension, self._valor_dimension, self._id_elemento]


class Esfuerzo(Entidad):

    @property
    def tipo_actividad(self):
        return self._tipo_actividad

    @tipo_actividad.setter
    def tipo_actividad(self, valor):
        if valor not in TIPO_ACTIVIDAD:
            raise("Error en el tipo de actividad")
        self._tipo_actividad = valor
        return

    @property
    def esfuerzo_actividad(self):
        return self._esfuerzo_actividad

    @esfuerzo_actividad.setter
    def esfuerzo_actividad(self, valor):
        self._esfuerzo_actividad = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self, tipo_actividad, esfuerzo_actividad, elemento):
        super().__init__()
        if tipo_actividad not in TIPO_ACTIVIDAD:
            raise("Error en el tipo de actividad")
        self._tipo_actividad = tipo_actividad
        self._esfuerzo_actividad = esfuerzo_actividad
        self._id_elemento = elemento
        return

    def __repr__(self):
        return str(self.tipo_actividad) + ": " + str(self.esfuerzo_actividad)


class Defecto(Entidad):

    @property
    def fase_defecto(self):
        return self._fase_defecto

    @fase_defecto.setter
    def fase_defecto(self, valor):
        if valor not in FASE_DEFECTO:
            raise ("Error en el tipo de fase")
        self._fase_defecto = valor
        return

    @property
    def cantidad_defecto(self):
        return self._cantidad_defecto

    @cantidad_defecto.setter
    def cantidad_defecto(self, valor):
        self._cantidad_defecto = valor
        return

    @property
    def identificacion_elemento(self):
        return self._id_elemento

    def __init__(self, fase_defecto, cantidad_defecto, elemento):
        super().__init__()
        if fase_defecto not in FASE_DEFECTO:
            raise("Error en el tipo de fase")
        self._fase_defecto = fase_defecto
        self._cantidad_defecto = cantidad_defecto
        self._id_elemento = elemento
        return

    def __repr__(self):
        return str(self.fase_defecto) + ": " + str(self.cantidad_defecto)


class NombreElemento(TextoNoVacio):

    def __rep__(self):
        return self.texto


class Elemento(Entidad):

    @property
    def nombre_elemento(self):
        return self._nombre_elemento

    @nombre_elemento.setter
    def nombre_elemento(self, valor):
        self._nombre_elemento = valor
        return

    @property
    def tipo_elemento(self):
        return self._tipo_elemento

    @tipo_elemento.setter
    def tipo_elemento(self, valor):
        if valor in TIPO_ELEMENTO:
            self._tipo_elemento = valor
        else:
            raise Exception("No es un tipo de elemento valido")
        return

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor
        return

    @property
    def id_componente(self):
        return self._id_componente

    @property
    def lista_dimensiones(self):
        return self._lista_dimensiones

    @property
    def lista_esfuerzos(self):
        return self._lista_esfuerzos

    @property
    def lista_defectos(self):
        return self._lista_defectos

    def __init__(self,  nombre, tipo_elemento, descripcion, componente):
        super().__init__()
        self._nombre_elemento = nombre
        if tipo_elemento in TIPO_ELEMENTO:
            self._tipo_elemento = tipo_elemento
        else:
            raise Exception("No es un tipo de elemnto valido")
        self._descripcion = descripcion
        self._id_componente = componente
        self._lista_dimensiones = []
        self._lista_esfuerzos = []
        self._lista_defectos = []
        return

    def agregar_dimension(self, dimension):
        self._lista_dimensiones.append([dimension, "NUEVO"])
        return

    def modificar_dimension(self, dimension_modificada):
        encontro = False
        for item in self._lista_dimensiones:
            dimension_buscada = item[0]
            if dimension_buscada.tipo_dimension == dimension_modificada.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [dimension_modificada, "CAMBIO"]
                encontro = True
        return encontro

    def eliminar_dimension(self, dimension_eliminada):
        encontro = False
        for item in self._lista_dimensiones:
            dimension_buscada = item[0]
            if dimension_buscada.tipo_dimension == dimension_eliminada.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [dimension_eliminada, "BORRADO"]
                encontro = True
        return encontro

    def agregar_esfuerzo(self, esfuerzo):
        self._lista_esfuerzos.append([esfuerzo, "NUEVO"])
        return

    def modificar_esfuerzo(self, esfuerzo_modificado):
        encontro = False
        for item in self._lista_esfuerzos:
            esfuerzo_buscado = item[0]
            if esfuerzo_buscado.tipo_dimension == esfuerzo_modificado.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [esfuerzo_modificado, "CAMBIO"]
                encontro = True
        return encontro

    def modificar_defecto(self, defecto_modificado):
        encontro = False
        for item in self._lista_defectos:
            defecto_buscado = item[0]
            if defecto_modificado.tipo_dimension == defecto_buscado.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [defecto_modificado, "CAMBIO"]
                encontro = True
        return encontro

    def agregar_defecto(self, defecto):
        self._lista_defectos.append([defecto, "NUEVO"])
        return

    def eliminar_esfuerzo(self, esfuerzo_eliminado):
        encontro = False
        for item in self._lista_dimensiones:
            esfuerzo_buscado = item[0]
            if esfuerzo_buscado.tipo_dimension == esfuerzo_eliminado.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [esfuerzo_eliminado, "BORRADO"]
                encontro = True
        return encontro

    def eliminar_defecto(self, defecto_eliminado):
        encontro = False
        for item in self._lista_defectos:
            defecto_buscado = item[0]
            if defecto_buscado.tipo_dimension == defecto_eliminado.tipo_dimension:
                indice = self._lista_dimensiones.index(item)
                self._lista_dimensiones[indice] = [defecto_eliminado, "BORRADO"]
                encontro = True
        return encontro

    def recuperar_dimension(self, dimension):
        self._lista_dimensiones.append([dimension, None])
        return

    def recuperar_esfuerzo(self, esfuerzo):
        self._lista_esfuerzos.append([esfuerzo, None])
        return

    def recuperar_defecto(self, defecto):
        self._lista_defectos.append([defecto, None])
        return

    def __repr__(self):
        return str(self.nombre_elemento) + ": " + self._tipo_elemento
