"""
Creacion iniciales de las tablas del modelo
"""
from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import *
from infraestructura.persistencia.modelo.base_de_datos_proyectos import Base

# Crea la conexión con el repositorio fisico de datos
DBEvaluacion = ContextoDBSQLite('sqlite:///proyectos.sqlite')

# Crea la tablas
DBEvaluacion.inicializar_tablas(Base)
