from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return ("Hola Mundo!")


@app.route("/suma")
def suma():
    return str(2 + 2)


@app.route("/mayuscula/<string:palabra>")
def mayuscula(palabra):
    return str(palabra).upper()


if __name__ == '__main__':
    app.run(debug=True)

