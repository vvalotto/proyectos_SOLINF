"""
Clase que inicializa y arma las instancias necesarias iniciales de la aplicaccion:
Contextos de datos
Respositorios
Gestores
"""
from infraestructura.persistencia.contexto.bd_sqlite.contexto_database_sqlite import ContextoDBSQLite
from infraestructura.persistencia.repositorios.DB_repositorio_proyecto import *
from infraestructura.persistencia.repositorios.DB_repositorio_componente import *
from infraestructura.persistencia.repositorios.DB_repositorio_elemento import *
from infraestructura.persistencia.mapeador.proyecto import *
from infraestructura.persistencia.mapeador.componente import *
from infraestructura.persistencia.mapeador.elemento import *
from aplicacion.gestores.gestor_proyecto import *
from aplicacion.gestores.gestor_componente import *
from aplicacion.gestores.gestor_elemento import *

from aplicacion.gestores.estadisticas_proyecto import EstadisticasProyecto
from dominio.analitica.muestra import Muestra

import os
directorio_base = os.path.abspath(os.path.dirname(__file__))
URI_DATABASE = 'sqlite:///' + os.path.join(directorio_base, 'proyectos.sqlite')


class Configurador:

    contexto = ContextoDBSQLite(URI_DATABASE)
    repositorio_proyecto = DBRepositorioProyecto(contexto, MapeadorDatosProyecto(contexto))
    repositorio_componente = DBRepositorioComponente(contexto, MapeadorDatosComponente(contexto))
    repositorio_elemento = DBRepositorioElemento(contexto, MapeadorDatosElemento(contexto))

    gestor_proyecto = GestorProyecto()
    gestor_proyecto.asignar_repositorio(repositorio_proyecto)

    gestor_componente = GestorComponente()
    gestor_componente.asignar_repositorio(repositorio_componente)

    gestor_elemento = GestorElemento()
    gestor_elemento.asignar_repositorio(repositorio_elemento)

    muestra_proyectos = Muestra("")
    estadisticas = EstadisticasProyecto("Sistema de Gestión de Flota", muestra_proyectos)
    repositorio = "proyectos.sqlite"
    datos_origen = "SELECT * FROM mediciones_proyecto;"
    muestra_proyectos.cargar_valores_de_muestra(repositorio, datos_origen)