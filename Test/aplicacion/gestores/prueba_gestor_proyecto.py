"""

"""
from aplicacion.gestores.gestor_proyecto import GestorProyecto

from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import ContextoDBSQLite
from infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from infraestructura.persistencia.mapeador.proyecto import *


# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')
mi_repositorio = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
print(mi_repositorio.contexto.recurso)

gestor = GestorProyecto()
gestor.asignar_repositorio(mi_repositorio)

nombre_proyecto = NombreProyecto('Sistema de Gestión de Flota')
gestor.crear_proyecto(nombre_proyecto, "DESARROLLO", "Sin Descripcion", "")
gestor.guardar_proyecto()

print("FIN")