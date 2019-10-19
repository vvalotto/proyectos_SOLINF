"""
--------------------------
Proyecto = ddd-evaluaciones
Modulo = prueba
Autor = admin
Fecha creación = 16/10/16
--------------------------
"""

from dominio.entidades.proyecto import *


#Prueba entidad proyecto

nombre_proyecto = NombreProyecto("Sistema de Gestión de Flota")
desc_proyecto = DescripcionProyecto("Sin Descripcion")
mi_proyecto = Proyecto(nombre_proyecto, "DESARROLLO", desc_proyecto, None)
print(mi_proyecto)
print(mi_proyecto.fecha_fin)
print(mi_proyecto.identificacion)

nombre_proyecto = NombreProyecto("hjkj")
desc_proyecto = DescripcionProyecto("jklkl")
mi_proyecto = Proyecto(nombre_proyecto, "", desc_proyecto, None)
print(mi_proyecto)
print(mi_proyecto.fecha_fin)
print(mi_proyecto.identificacion)