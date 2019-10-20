

class ListaProyectoVM:

    def __init__(self, gestor):
        self._gestor = gestor
        self._proyectos = []
        return

    def obtener_proyectos(self):
        return self._gestor.obtener_todos_los_proyectos()
