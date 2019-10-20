from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route("/")
def index():
    user = {'nombre': 'Python'}
    return render_template("index.html", usuario=user)


@app.route("/suma")
def suma():
    return str(2 + 2)


@app.route("/mayuscula/<string:palabra>")
def mayuscula(palabra):
    if len(palabra) < 2:
        return render_template("500.html")
    return str(palabra).upper()


if __name__ == '__main__':
    app.run(debug=True)

