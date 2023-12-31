# Ponderada Sprint 2

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Caio Martins de Abreu | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦 WebApp
 ┣ 📂api
 ┃ ┃ ┗ 📜main.cpython-311.pyc
 ┃ ┣ 📂auth
 ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┣ 📜jwt_bearer.py
 ┃ ┃ ┗ 📜jwt_handler.py
 ┃ ┣ 📂config
 ┃ ┃ ┗ 📜db.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┣ 📜todo_table.py
 ┃ ┃ ┗ 📜user_table.py
 ┃ ┣ 📂schemas
 ┃ ┃ ┣ 📜index.py
 ┃ ┃ ┣ 📜todo.py
 ┃ ┃ ┣ 📜user.py
 ┃ ┃ ┗ 📜userlogin.py
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂assets
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┣ 📜todo.html
 ┃ ┃ ┗ 📜user.html
 ┃ ┣ 📜.env
 ┃ ┣ 📜.gitignore
 ┃ ┣ 📜Dockerfile
 ┃ ┣ 📜main.py
 ┃ ┗ 📜requirements.txt
 ┣ 📂database
 ┃ ┣ 📜Dockerfile
 ┃ ┗ 📜init.sql
 ┣ 📜READEME.md
 ┗ 📜docker-compose.yml
```

## Explicação do Projeto
A atividade atesta a capacidade do aluno de lidar com múltiplos containers e criar uma aplicação web simples que contenha um CRUD de usuários e um CRUD de tarefas. O projeto foi realizado utilizando Python, o framework FastAPI e o template engine Jinja2 para servir os arquivos estáticos. O banco de dados utilizado foi o MySQL. 

## Como Rodar o Projeto
### Localmente
Fazendo a build da imagem contida arquivo Dockerfile, o projeto pode ser executado com o seguinte comando em um terminal de sua preferência, desde que na raíz do projeto:
```
docker compose up -d --build
```
Após isso, projeto pode ser acessado em **[localhost](http://localhost:5000)**.

> [!NOTE]  
> As imagens utilizadas podem ser acessadas nos dockerhub nos links **[database](https://hub.docker.com/r/cmtabr/db)** e **[api](https://hub.docker.com/r/cmtabr/api)**

> [!WARNING]
> Tive alguns problemas com o banco de dados, backend sempre iniciando previamente, desta forma a tag restart foi enderaçada como always para reiniciar a aplicação até que o banco tenha sido construído.
