"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from infraestructura.persistencia.contexto.contexto_database import ContextoDB


class ContextoDBSQLite(ContextoDB):
    """
    Contexto que se especializa en la conexión con SQlite
    """

    def __init__(self, recurso):
        super().__init__(recurso)
        return
