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


class ComponenteForm(FlaskForm):
    nombre_componente = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    tipo_componente = StringField('Tipo de Componente')
    id = StringField('Identificador')
    id_proyecto = StringField('Id_Proyecto')
    proyecto = StringField('Proyecto')
    lista_elementos = []

    @staticmethod
    def inicializar():
        ComponenteForm.nombre_componente = None
        ComponenteForm.tipo_componente = None
        ComponenteForm.id = None
        ComponenteForm.id_proyecto = None
        ComponenteForm.proyecto = None
        ComponenteForm.lista_elementos = []


class ElementoForm(FlaskForm):
    nombre_elemento = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    tipo_elemento = StringField('Tipo del Elemento')
    descripcion = StringField('Descripcion')
    id = StringField('Identificador')
    id_componente = StringField('Id_Proyecto')
    dimensiones = []
    esfuerzos = []
    defectos = []
    proyecto = StringField('Proyecto')
    componente = StringField("Componente")

    @staticmethod
    def inicializar():
        ElementoForm.nombre_elemento = None
        ElementoForm.tipo_elemento = None
        ElementoForm.descripcion = None
        ElementoForm.id_componente = None
        ElementoForm.id = None
        ElementoForm.dimensiones = []
        ElementoForm.esfuerzos = []
        ElementoForm.defectos = []
        ElementoForm.proyecto = None
        ElementoForm.componente = None