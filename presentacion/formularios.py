from flask_wtf import FlaskForm


class ListaProyectoForm(FlaskForm):
    lista_proyectos = []

    @staticmethod
    def inicializar():
        ListaProyectoForm.lista_proyectos = []
