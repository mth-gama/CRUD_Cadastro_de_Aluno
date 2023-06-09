# CRUD_Cadastro_de_Aluno
## Infos

- :package: novas funcionalidades
- :up: atualizações 
- :ant: correção de bug
- :checkered_flag: release

# Requirements

Libs
- mysql==0.0.3
- mysql-connector==2.2.9
- mysql-connector-python==8.0.33
- mysqlclient==2.1.1
- protobuf==3.20.3

MySQL
- MySQL Worckbanch version 8.0.25

# How to use 
First step
- pip install requirements.txt

Second step
In Worckbanch
- Exceute command for creating database and tables
CREATE DATABASE crud;

CREATE TABLE aluno(
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    curso VARCHAR(255) NOT NULL,
    valor_curso FLOAT NOT NULL,
    PRIMARY KEY (id)
);

## Screenshot

None

## Author

- Website - [Matheus Gama](https://mth-gama.github.io/)
- GitHub - [@mth-gama](https://github.com/mth-gama)

## Acknowledgments

Projeto solo
