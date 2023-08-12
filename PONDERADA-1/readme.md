# Ponderada Sprint 1 

# Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Caio Martins de Abreu | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦Curriculum Vitae
 ┣ 📂static
 ┃ ┣ 📂assets
 ┃ ┃ ┗ 📜Img.jpeg
 ┃ ┃ ┗ 📜...
 ┃ ┗ 📂css
 ┃ ┃ ┗ 📜styles.css
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜main.py
 ┣ 📜readme.md
 ┗ 📜requirements.txt
```
## Explicação do Projeto
A atividade atesta a capacidade do aluno de fazer um portfolio básico conteinerizado com Docker. O projeto foi realizado utilizando Python, o framework FastAPI e o template engine Jinja2 para servir os arquivos estáticos. 

## Como Rodar o Projeto
### Localmente
Faznedo o build da imagem contida arquivo Dockerfile, o projeto pode ser executado com o seguinte comando em um terminal de sua preferência:
```
docker build -t <nome-da-sua-imagem> .
docker run -d --name <nome-do-seu-container> -p 80:80 <nome-da-sua-imagem>
```
Após isso, projeto pode ser acessado em **[localhost](http://localhost:80)**.

### Via Docker Hub
Fazendo o pull da imagem contido no Docker Hub, **[Curriculum Vitae](https://hub.docker.com/r/cmtabr/curriculum-vitae)**, o projeto pode ser executado com o seguinte comando em um terminal de sua preferência:
```
docker pull cmtabr/curriculum-vitae:v0.0.1
docker run -d -p 80:80 cmtabr/curriculum-vitae:v0.0.1
```
Após isso, projeto pode ser acessado em **[localhost](http://localhost:80)**.

