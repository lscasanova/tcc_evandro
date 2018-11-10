# API para consulta ao banco de alunos

## Consultar todos os alunos
GET http://servidor-tcc.herokuapp.com/alunos

## Consultar aluno pelo RA
GET http://servidor-tcc.herokuapp.com/aluno/$ra

## Vincular uuid do bluetooth ao aluno
PUT http://servidor-tcc.herokuapp.com/alunos/cadastro/20606884

Body: {"uuid":"khasdlkasdlkasskhdklklda"}' 

## Registrar data e hora do login do aluno
PUT http://servidor-tcc.herokuapp.com/alunos/logon/khasdlkasdlkasskhdklklda

Body: '{"data_hora":"20181107195200"}' 

## Registrar data e hora do logoff do aluno
PUT http://servidor-tcc.herokuapp.com/alunos/logoff/khasdlkasdlkasskhdklklda

Body: '{"data_hora":"20181107201100"}' 