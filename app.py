#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

alunos = [
    {
        'id': 1,
        'uuid':'',
        'ra': u'20606884',
        'nome': u'EVANDRO DOS SANTOS', 
        'cpf': u'37160902807',
        'data_hora_login':"",
        'data_hora_logoff':"",
    },
    {
        'id': 2,
        'uuid':'',
        'ra': u'20547540',
        'nome': u'RUTE CARDOSO', 
        'cpf': u'37160902806',
        'data_hora_login':"",
        'data_hora_logoff':"",
    },
    {
        'id': 3,
        'uuid':'',
        'ra': u'20904866',
        'nome': u'RAFAEL OKADA', 
        'cpf': u'37160902805',
        'data_hora_login':"",
        'data_hora_logoff':"",
    }
]

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'alunos': alunos})


@app.route('/alunos/ra/<aluno_ra>', methods=['GET'])
def get_aluno_ra(aluno_ra):
    aluno = [aluno for aluno in alunos if aluno['ra'] == aluno_ra]
    if len(aluno) == 0:
        abort(404)
    return jsonify({'aluno': aluno[0]})

@app.route('/alunos/cpf/<aluno_cpf>', methods=['GET'])
def get_aluno_cpf(aluno_cpf):
    aluno = [aluno for aluno in alunos if aluno['cpf'] == aluno_cpf]
    if len(aluno) == 0:
        abort(404)
    return jsonify({'aluno': aluno[0]})

@app.route('/alunos/nome/<aluno_nome>', methods=['GET'])
def get_aluno_nome(aluno_nome):
    aluno = [aluno for aluno in alunos if aluno['nome'] == aluno_nome]
    if len(aluno) == 0:
        abort(404)
    return jsonify({'aluno': aluno[0]})

@app.route('/alunos/cadastro/<aluno_ra>', methods=['PUT'])
def update_aluno(aluno_ra):
    aluno = [aluno for aluno in alunos if aluno['ra'] == aluno_ra]
    if len(aluno) == 0:
        abort(404)
    if not request.json:
        abort(400)

    aluno[0]['uuid'] = request.json.get('uuid', aluno[0]['uuid'])
    return jsonify({'aluno': aluno[0]}), 201

@app.route('/alunos/logon/<aluno_uuid>', methods=['PUT'])
def logon_aluno(aluno_uuid):
    aluno = [aluno for aluno in alunos if aluno['uuid'] == aluno_uuid]
    if len(aluno) == 0:
        abort(404)
    if not request.json:
        abort(400)

    lista_horarios = []
    aluno[0]['data_hora_login'] = request.json.get('data_hora', aluno[0]['data_hora_login'])
    return jsonify({'aluno': aluno[0]}), 201

@app.route('/alunos/logoff/<aluno_uuid>', methods=['PUT'])
def logoff_aluno(aluno_uuid):
    aluno = [aluno for aluno in alunos if aluno['uuid'] == aluno_uuid]
    if len(aluno) == 0:
        abort(404)
    if not request.json:
        abort(400)

    lista_horarios = []
    aluno[0]['data_hora_logoff'] = request.json.get('data_hora', aluno[0]['data_hora_logoff'])
    return jsonify({'aluno': aluno[0]}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
