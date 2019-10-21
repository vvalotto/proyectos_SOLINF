from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

tareas = [
    {
        'id': 1,
        'titulo': u'Core Python Application Programming',
        'descripcion': u'Muy buen libro para programación avanzada',
        'done': False
    },
    {
        'id': 2,
        'titulo': u'Learn Python',
        'descripcion': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.errorhandler(404)
def not_fount(error):
    return make_response(jsonify({'error': 'No encontrado'}), 404)


@app.route('/tareas/<int:tarea_id>', methods=['GET'])
def get_tarea(tarea_id):
    tarea = [tarea for tarea in tareas if tarea['id'] == tarea_id]
    if len(tarea) == 0:
        abort(404)
    return jsonify({'tarea': tarea[0]})


@app.route('/tareas/', methods=['POST'])
def post_tarea():
    r = request
    if not request.json or not 'titulo' in request.json:
        abort(400)
    tarea = {
        'id': tareas[-1]['id'] + 1,
        'titulo': request.json['titulo'],
        'descripcion': request.json.get('descripcion', ""),
        'done': False
    }
    tareas.append(tarea)
    return jsonify({'tarea': tarea}), 201


if __name__ == '__main__':
    app.run(debug=True)
