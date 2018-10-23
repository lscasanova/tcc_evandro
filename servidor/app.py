#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

alunos = [
    {
        'id': 1,
        'ra': u'20606884',
        'nome': u'EVANDRO DOS SANTOS', 
        'cpf': u'37160902807'
    },
    {
        'id': 2,
        'ra': u'20547540',
        'nome': u'RUTE CARDOSO', 
        'cpf': u'37160902806'
    },
    {
        'id': 3,
        'ra': u'20904866',
        'nome': u'RAFAEL OKADA', 
        'cpf': u'37160902805'
    }
]

@app.route('/tcc/api/v1.0/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'alunos': alunos})


@app.route('/tcc/api/v1.0/alunos/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = [aluno for aluno in alunos if aluno['id'] == aluno_id]
    if len(aluno) == 0:
        abort(404)
    return jsonify({'aluno': aluno[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
