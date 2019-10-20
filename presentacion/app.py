from flask import Flask, render_template, request,redirect, url_for
from flask_bootstrap import Bootstrap
from presentacion.formularios import ListaProyectoForm, ProyectoForm
from presentacion.modelos import ListaProyectoVM, ProyectoVM
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
    formulario = ProyectoForm()
    formulario.inicializar()
    proyecto = ProyectoVM(config.gestor_proyecto)

    if id != "0":
        if request.method == "GET":
            if proyecto.recuperar_proyecto(id) is None:
                return redirect(url_for("index"))
            else:
                proyecto.listar_modulos()
                formulario.id = proyecto.identificador
                formulario.nombre_proyecto = proyecto.nombre
                formulario.descripcion = proyecto.descripcion
                formulario.tipo_proyecto = proyecto.tipo
                formulario.fecha_fin = proyecto.fecha_fin

                for item in proyecto.lista:
                    formulario.lista_modulos.append(item)
    else:
        if request.method == "POST":
            nombre_proyecto = request.form.get("nombre_proyecto")
            tipo_proyecto = request.form.get("tipo_proyecto")
            descripcion = request.form.get("descripcion")
            fecha_fin = request.form.get("fecha_fin")
            proyecto.agregar_proyecto(nombre_proyecto, tipo_proyecto, descripcion, fecha_fin)
            return redirect("/proyectos/")
        else:
            formulario.id = id

    return render_template("proyecto.html", form=formulario)


@app.route("/componente/", methods=["POST"])
@app.route("/componente/<string:id>/", methods=["GET", "POST"])
def componente(id):
    return


if __name__ == '__main__':
    config = Configurador
    app.run(debug=True)
