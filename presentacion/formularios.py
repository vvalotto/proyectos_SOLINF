from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ListaProyectoForm(FlaskForm):
    lista_proyectos = []

    @staticmethod
    def inicializar():
        ListaProyectoForm.lista_proyectos = []


class ProyectoForm(FlaskForm):
    nombre_proyecto = StringField('Nombre del Proyecto', validators=[DataRequired(), Length(max=50)])
    descripcion = StringField('Descripcion')
    tipo_proyecto = StringField('Tipo de Proyecto')
    fecha_fin = StringField('Fecha de Fin')
    id = StringField('Identificador')
    lista_modulos = []

    @staticmethod
    def inicializar():
        ProyectoForm.nombre_proyecto = None
        ProyectoForm.descripcion = None
        ProyectoForm.tipo_proyecto = None
        ProyectoForm.fecha_fin = None
        ProyectoForm.lista_modulos = []