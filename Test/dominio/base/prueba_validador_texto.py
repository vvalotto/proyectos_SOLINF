from dominio.base.texto_no_vacio import *

if __name__ == "__main__":
    texto = None
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = ""
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = '1'
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = 'a'
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = 'asssd'
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = 1
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = 2.1
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = []
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)

    texto = {}
    validacion = ValidadorTexto().validar(texto)
    print(validacion.valido)
    print(validacion.resultado)
