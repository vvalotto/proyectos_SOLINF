"""
Clase que inicializa y arma las instancias necesarias iniciales de la aplicaccion:
Contextos de datos
Respositorios
Gestores
"""
from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import *
from infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from infraestructura.persistencia.mapeador.proyecto import *
from aplicacion.gestores.gestor_proyecto import *

import os
directorio_base = os.path.abspath(os.path.dirname(__file__))
URI_DATABASE = 'sqlite:///' + os.path.join(directorio_base, 'proyectos.sqlite')


class Configurador:

    contexto = ContextoDBSQLite(URI_DATABASE)
    repositorio_proyecto = DBRepositorioProyecto(contexto, MapeadorDatosProyecto(contexto))

    gestor_proyecto = GestorProyecto()
    gestor_proyecto.asignar_repositorio(repositorio_proyecto)
