from dominio.analitica.muestra import Muestra
from dominio.analitica.analizador import Analizador


muestra = Muestra("Sistema de Gestión de Flota")

repositorio = "proyectos.sqlite"
datos_origen = "SELECT * FROM mediciones_proyecto;"
muestra.cargar_valores_de_muestra(repositorio, datos_origen)


esfuerzo_total = muestra.obtener_esfuerzo_total_proyecto()
print("Esfuerzo total del proyecto: %5.2f Horas o %5.2f PM" %(esfuerzo_total, (esfuerzo_total/152) ))

esfuerzos = muestra.obtener_esfuerzo_por_actividad()
for actividad, esfuerzo in esfuerzos.items():
    print("Para %s: %5.2f horas" %(actividad, esfuerzo))

print('Cantidad de defectos: %3i' %muestra.obtener_cantidad_defectos())

analizador = Analizador(muestra)
x = muestra.obtener_dimensiones_proyecto()
y = muestra.obtener_clases_CU()
print(x)
print(y)
analizador.clasificar_tamanio(x, y)
clases_tamanio = {}
clases_tamanio['simple'] = 5
clases_tamanio['media'] = 10
clases_tamanio['compleja'] = 15
print(clases_tamanio)
t = int(analizador.predicir_tamanio(1, 1, 0)[0])

for clave, valor in clases_tamanio.items():
    if valor == t:
        complejidad = clave
        break
print(complejidad)