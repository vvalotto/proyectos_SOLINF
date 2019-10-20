from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from presentacion.formularios import ListaProyectoForm
from presentacion.modelos import ListaProyectoVM
from presentacion.configurador import *

app = Flask(__name__)
boostrap = Bootstrap(app)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/proyectos/")
def proyecto_lista():
    formulario = ListaProyectoForm()
    formulario.inicializar()
    lista_proyectos = ListaProyectoVM(config.gestor_proyecto)
    for item in lista_proyectos.obtener_proyectos():
        formulario.lista_proyectos.append(item)
    return render_template("proyectos.html", form=formulario)


app.route("/proyecto/", methods=["POST"])
@app.route("/proyecto/<string:id>", methods=["GET", "POST"])
def proyecto(id):
    return


if __name__ == '__main__':
    config = Configurador
    app.run(debug=True)
