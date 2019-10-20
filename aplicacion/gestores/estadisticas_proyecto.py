"""
Clase que realiza los cálculos para el proyecto de acuerdo a la muestra seleccionda
"""


class EstadisticasProyecto:

    @property
    def productividad(self):
        return self._muestra.obtener_esfuerzo_total_proyecto() / self._muestra.obtener_tamanio_en_ucp()

    @property
    def densidad_de_defectos(self):
        return self._muestra.obtener_cantidad_de_defectos() / self._muestra.obtener_tamanio_en_ucp()

    @property
    def cantidad_de_defectos(self):
        return self._muestra.obtener_cantidad_de_defectos()

    @property
    def tamanio_real_UCP(self):
        return self._muestra.obtener_tamanio_en_ucp()

    @property
    def esfuerzo_real(self):
        return self._muestra.obtener_esfuerzo_total_proyecto()

    @property
    def distribucion_esfuerzos(self):
        return self._calcular_distribucion_esfuerzo()

    def __init__(self, proyecto, muestra):
        self._proyecto = proyecto
        self._muestra = muestra
        return

    def _calcular_distribucion_esfuerzo(self):
        esfuerzo_total = self._muestra.obtener_esfuerzo_total_proyecto()
        esfuerzos = self._muestra.obtener_esfuerzo_por_actividad()
        distribucion = {}
        for key in esfuerzos.keys():
            distribucion[key] = (esfuerzos[key] / esfuerzo_total) * 100
        return distribucion
