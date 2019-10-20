"""

"""
from aplicacion.gestores.gestor_proyecto import GestorProyecto
from aplicacion.gestores.gestor_componente import GestorComponente
from aplicacion.gestores.gestor_elemento import GestorElemento

from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import ContextoDBSQLite
from infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from infraestructura.persistencia.mapeador.proyecto import *

from infraestructura.persistencia.repositorios.DB_repositorio_componente import *
from infraestructura.persistencia.mapeador.componente import *

from infraestructura.persistencia.repositorios.DB_repositorio_elemento import *
from infraestructura.persistencia.mapeador.elemento import *

# Crea el contexto para el repositorio de la entidades
mi_contexto = ContextoDBSQLite('sqlite:///proyectos.sqlite')
repo_proyecto = DBRepositorioProyecto(mi_contexto, MapeadorDatosProyecto(mi_contexto))
print(repo_proyecto.contexto.recurso)

gestor = GestorProyecto()
gestor.asignar_repositorio(repo_proyecto)

nombre_proyecto = NombreProyecto('Sistema de Gestión de Flota')
gestor.crear_proyecto(nombre_proyecto, "DESARROLLO", "Sin Descripcion", "")
proyecto = gestor.recuperar_proyecto_por_nombre(str(nombre_proyecto))

print("Proyecto Recuperado:")
print(proyecto)

repo_componente = DBRepositorioComponente(mi_contexto, MapeadorDatosComponente(mi_contexto))
gestor_componente = GestorComponente()
gestor_componente.asignar_repositorio(repo_componente)

nombre_componente = NombreComponente("Mi componente")
componente = gestor_componente.recuperar_componente_por_nombre("Mi componente")
print("Componente Recuperado:")
print(componente.nombre)

repo_elemento = DBRepositorioElemento(mi_contexto, MapeadorDatosElemento(mi_contexto))
gestor_elemento = GestorElemento()
gestor_elemento.asignar_repositorio(repo_elemento)

nombre_elemento = NombreElemento("Mi elemento")
elemento = gestor_elemento.recuperar_elemento_por_nombre(str(nombre_elemento))

print("Elemento recuperado")
print(elemento.nombre_elemento)

gestor_elemento.dimensionar_elemento("Entidades", 5)
gestor_elemento.guardar_elemento()

elemento = gestor_elemento.recuperar_elemento_por_nombre(str(nombre_elemento))

print(elemento.lista_dimensiones)

print("FIN")