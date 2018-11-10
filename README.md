tcc_evandro

curl -i -H GET http://servidor-tcc.herokuapp.com/alunos

curl -i -H GET http://servidor-tcc.herokuapp.com/aluno/<ra>

curl -i -H "Content-Type: application/json" -X PUT -d '{"uuid":"khasdlkasdlkasskhdklklda"}' http://servidor-tcc.herokuapp.com/alunos/cadastro/20606884

curl -i -H "Content-Type: application/json" -X PUT -d '{"data_hora":"20181107195200"}' http://servidor-tcc.herokuapp.com/alunos/logon/khasdlkasdlkasskhdklklda

curl -i -H "Content-Type: application/json" -X PUT -d '{"data_hora":"20181107201100"}' http://servidor-tcc.herokuapp.com/alunos/logoff/khasdlkasdlkasskhdklklda

# Cadastro de usuário
curl -i -H "Content-Type: application/json" -X POST -d '{"nome":"LEANDRO DOS SANTOS","ra":"12345678", "cpf":"31774917807"}' http://localhost:5000/aluno/cadastro