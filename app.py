#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    ra = db.Column(db.String(8), unique=True, nullable=False)
    uuid = db.Column(db.String(32), unique=True)
    data_hora_login = db.Column(db.String(14), unique=True)
    data_hora_logoff = db.Column(db.String(14), unique=True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    dict_aluno = {}
    list_alunos = []
    for aluno in alunos:
        dict_aluno = ({'nome': aluno.nome,
                              'ra': aluno.ra,
                              'cpf': aluno.cpf,
                              'uuid': aluno.uuid,
                              'data_hora_login': aluno.data_hora_login,
                              'data_hora_logoff': aluno.data_hora_logoff,
                             })
        list_alunos.append(dict_aluno)
    json_alunos = jsonify({'alunos': list_alunos})
    return json_alunos


@app.route('/aluno/<aluno_ra>', methods=['GET'])
def get_aluno_ra(aluno_ra):
    aluno = Aluno.query.filter_by(ra=aluno_ra).first_or_404()
    return jsonify({'nome': aluno.nome,
                    'ra': aluno.ra,
                    'cpf': aluno.cpf,
                    'uuid': aluno.uuid,
                    'data_hora_login': aluno.data_hora_login,
                    'data_hora_logoff': aluno.data_hora_logoff,
                    })


@app.route('/aluno/cadastro', methods=['POST'])
def cadastro_aluno():
    aluno = Aluno(nome=request.json.get('nome'),
                  cpf=request.json.get('cpf'),
                  ra=request.json.get('ra')
    )
    db.session.add(aluno)
    db.session.commit()

    return jsonify(success=True), 200


@app.route('/aluno/cadastro/<aluno_ra>', methods=['PUT'])
def update_aluno(aluno_ra):
    aluno = Aluno.query.filter_by(ra=aluno_ra).first_or_404()
    aluno.uuid = request.json.get('uuid')
    db.session.add(aluno)
    db.session.commit()

    return jsonify(success=True), 201


@app.route('/aluno/logon/<aluno_uuid>', methods=['PUT'])
def logon_aluno(aluno_uuid):
    aluno = Aluno.query.filter_by(uuid=aluno_uuid).first_or_404()
    
    aluno.data_hora_login = request.json.get('data_hora')
    db.session.add(aluno)
    db.session.commit()
    
    return jsonify(success=True), 201

@app.route('/aluno/logoff/<aluno_uuid>', methods=['PUT'])
def logoff_aluno(aluno_uuid):
    aluno = Aluno.query.filter_by(uuid=aluno_uuid).first_or_404()
    
    aluno.data_hora_logoff = request.json.get('data_hora')
    db.session.add(aluno)
    db.session.commit()
    
    return jsonify(success=True), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
