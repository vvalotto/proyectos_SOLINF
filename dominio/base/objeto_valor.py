"""
Objeto Valor Generico
"""
from abc import ABCMeta, abstractmethod


class ObjetoValor(metaclass=ABCMeta):


    @abstractmethod
    def obtener_atributos_incluidos_en_chequeo_igualdad(self):
        pass

    def __eq__(self, otro):
        '''
        Evalua la igualdad de dos Objetos Valor
        :param otro: OV contra el que se quiere comparar (izquierda del == )
        :return: Verdadero o falso
        '''
        if otro is None:
            return False

        return self.obtener_atributos_incluidos_en_chequeo_igualdad() == \
            otro.obtener_atributos_incluidos_en_chequeo_igualdad()

    def __ne__(self, otro):
        """
        Evalua la desigualdad de dos Objetos Valot
        :param otro: OV contra el que se quiere comparar (izquierda del == )
        :return: Verdadero o falso
        """
        return not(self.__eq__(otro))






