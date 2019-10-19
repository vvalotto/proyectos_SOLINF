"""

"""
from aplicacion.gestores.gestor_proyecto import GestorProyecto
from aplicacion.gestores.gestor_componente import GestorComponente
from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import ContextoDBSQLite
from infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from infraestructura.persistencia.mapeador.proyecto import *

from infraestructura.persistencia.repositorios.DB_repositorio_componente import *
from infraestructura.persistencia.mapeador.componente import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')
repo_proyecto = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
print(repo_proyecto.contexto.recurso)

gestor = GestorProyecto()
gestor.asignar_repositorio(repo_proyecto)

nombre_proyecto = NombreProyecto('Sistema de Gestión de Flota')
gestor.crear_proyecto(nombre_proyecto, "DESARROLLO", "Sin Descripcion", "")
proyecto = gestor.recuperar_proyecto_por_nombre(str(nombre_proyecto))

print(proyecto.identificacion)

repo_componente = DBRepositorioComponente(mi_contexto, MapeadorDatosComponente(mi_contexto))
gestor_componente = GestorComponente()
gestor_componente.asignar_repositorio(repo_componente)

nombre_componente = NombreComponente("Mi componente")
gestor_componente.crear_componente(nombre_componente, "Módulo", proyecto.identificacion)
gestor_componente.guardar_componente()
print("FIN")