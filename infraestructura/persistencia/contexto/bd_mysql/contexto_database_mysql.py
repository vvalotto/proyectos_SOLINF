"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""
import pymysql


class ContextoDBMySQL(ContextoDB):
    """
    Contexto que se especializa en la conexión con MySQL
    """
    def __init__(self, recurso):
        pymysql.install_as_MySQLdb()
        super().__init__(recurso)
        return