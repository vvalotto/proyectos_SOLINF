from dominio.analitica.muestra import Muestra
from aplicacion.gestores.estadisticas_proyecto import *

muestra = Muestra("Sistema de Gestión de Flota")

repositorio = "proyectos.sqlite"
datos_origen = "SELECT * FROM mediciones_proyecto;"
muestra.cargar_valores_de_muestra(repositorio, datos_origen)

estadistica = EstadisticasProyecto("Sistema de Gestión de Flota", muestra)

print('Productividad: %5.2f UPC/hrs' %estadistica.productividad)
print('Densidad de Defectos: %5.2f Defectos/UCP' %estadistica.densidad_de_defectos)
print('Esfuerzo/Costo: %5.2f HH' %estadistica.esfuerzo_real)

print('Distribución Esfuerzo(%):')
for actividad, esfuerzo in estadistica.distribucion_esfuerzos.items():
    print('%s: %5.2f' %(actividad, esfuerzo))