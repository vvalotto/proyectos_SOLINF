"""
Clase Abstracta que define los metodos claves de la especificacion
"""


class BaseEspecificacion:

    def __init__(self, objeto):
        self._objeto = objeto
        return

    def es_satifecho_por(self, objeto):
        pass

    def y(self, especificacion):
        pass

    def o(self, especificacion):
        pass

    def no(self, especificacion):
        pass


"""
Clases Abstracta que implementan y(), o(), no()
"""


class BaseEspecificacionCompuesta(BaseEspecificacion):

    def y(self, especificacion):
        return Yespecificacion(self, especificacion)

    def o(self, especificacion):
        return Oespecificacion(self, especificacion)

    def no(self, especificacion):
        return NOespecificacion(especificacion)


class Yespecificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec_izquierda, espec_derecha):
        self._espec_izquierda = espec_izquierda
        self._espec_derecha = espec_derecha
        return

    def es_satifecho_por(self, objeto):
        return self._espec_izquierda.es_satisfecho_por(objeto) and\
               self._espec_derecha.es_satisfecha_por(objeto)


class Oespecificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec_izquierda, espec_derecha):
        self._espec_izquierda = espec_izquierda
        self._espec_derecha = espec_derecha
        return

    def es_satifecho_por(self, objeto):
        return self._espec_izquierda.es_satisfecho_por(objeto) or\
               self._espec_derecha.es_satisfecha_por(objeto)


class NOespecificacion(BaseEspecificacionCompuesta):

    def __init__(self, espec):
        self._espec = espec
        return

    def es_satifecho_por(self, objeto):
        return not(self._espec.es_satisfecho_por(objeto))


"""
Aplica el patron Specification a una Entidad
"""
from abc import *


class BaseEspecificacion(metaclass=ABCMeta):
    """
    Define la interfaz para el uso del patron
    """
    @abstractmethod
    def es_satisfecho_por(self, candidata):
        """
        Define el criterio con que se debe
        satifacer el requerimiento sobre la entidad
        candidata
        :param candidata: Entidad sobre la que se evalua
        :return: Booleano si cumple o no el requerimiento
        """

    def y(self, otra):
        """
        Define el conjuncion Y para determinar
        especificaciones compuestas
        :param otra: La otra especificacion con la que se
        requiere componer y cumplir
        :return: Especificacion
        """
        return YEspecificacion(self, otra)

    def o(self, otra):
        """
        Define el conjuncion O para determinar
        especificaciones compuestas
        :param otra: La otra especificacion con la que se
        requiere componer y cumplir
        :return: Especificacion
        """
        return OEspecificacion(self, otra)

    def no(self):
        """
        Define y no cumplimiento de la especificacion
        :return: Especificacion
        """
        return NOEspecificacion(self)


class EspecificacionCompuesta(BaseEspecificacion):
    """
    Define la estrucura interna con dos
    especificaciones para evaluar ambas
    """
    def __init__(self, espec_izquierda, espec_derecha):
        """
        Inicializa la instancia de especificacion
        :param espec_izquierda:
        :param espec_derecha:
        """
        self._izquierda = espec_izquierda
        self._derecha = espec_derecha
        return


class YEspecificacion(EspecificacionCompuesta):
    """
    Define la Especificacion Compuesta Y
    """
    def __init__(self, espec_izquierda, espec_derecha):
        super().__init__(espec_izquierda, espec_derecha)

    def es_satisfecho_por(self, candidata):
        """
        Determina si la especficacion es satifecha, ejecuta
        una validacion que las dos especificaciones sean
        verdaderas
        :param candidata:
        :return: booleano
        """
        return self._izquierda.es_satisfecho_por(candidata) and\
            self._derecha.es_satisfecho_por(candidata)


class OEspecificacion(EspecificacionCompuesta):
    """
    Define la Especificacion Compuesta O
    """
    def __init__(self, espec_izquierda, espec_derecha):
        super().__init__(espec_izquierda, espec_derecha)

    def es_satisfecho_por(self, candidata):
        """
        Determina si la especficacion es satifecha, ejecuta una
        validacion que alguna de las dos especificaciones sean
        verdaderas
        :param candidata:
        :return: booleano
        """
        return self._izquierda.es_satisfecho_por(candidata) or\
            self._derecha.es_satisfecho_por(candidata)


class NOEspecificacion(BaseEspecificacion):
    """
    Define la Especificacion No
    """
    def __init__(self, especificacion):
        self._especificacion = especificacion

    def es_satisfecho_por(self, candidata):
        """
        Determina si la especficacion es satifecha cuando
        no cumple con el requerimiento
        :param candidata:
        :return: booleano
        """
        return not self._especificacion.es_satisfecho_por(candidata)
