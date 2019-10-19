"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from sqlalchemy import create_engine
from .contexto import BaseContexto


class ContextoDB(BaseContexto):
    """
    Implementa un contexto correspodiente a un motor de base de datos
    """

    @property
    def recurso(self):
        return self._recurso

    def __init__(self, recurso):
        """
        :param recurso:El recurso corresponde al nombre y motor de la base de datos
        :return:
        """
        super().__init__(recurso)
        self._recurso = create_engine(recurso)
        self._recurso.echo = False

    def inicializar_tablas(self, base):
        """
        Crear las tablas
        :return:
        """
        base.metadata.bind = self._recurso
        base.metadata.create_all()
