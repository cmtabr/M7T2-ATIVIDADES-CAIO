# Ponderada 3 - M7T2 
## Desenvolvimento de Aplicação Web Conteínerizada e Deploy em Nuvem

### Informações do Aluno  
Aluno | Curso | Módulo | Turma
:---: | :---: | :---: | :---:
Caio Martins de Abreu | Engenharia da Computação | 7 | 2

## Estrutura de Pastas
```
📦 WebApp Stroke Prediction
 ┣ 📂data
 ┃  ┣ 📜stroke_data.csv
 ┃  ┗ 📜treatment.ipynb 
 ┣ 📂ml
 ┃ ┗ 📜model.pkl
 ┣ 📂static
 ┃ ┗ 📂css
 ┃   ┗ 📜style.css
 ┣ 📂templates
 ┃ ┗📜index.html
 ┣ 📜.dockerignore
 ┣ 📜requirements.txt
 ┣ 📜main.py
 ┣ 📜READEME.md
 ┗ 📜Dockerfile.yml
```

## Descrição do Projeto
Com o intuito de avaliar a capacidade do aluno de desenvolver uma aplicação web contêinerizada e realizar o deploy em nuvem, foi proposto o desenvolvimento de uma aplicação web que realiza a predição de um AVC (Acidente Vascular Cerebral) baseado em dados de pacientes. Para isso, foi utilizado o dataset [Stroke Prediction Dataset](https://www.kaggle.com/datasets/prosperchuks/health-dataset?resource=download&select=stroke_data.csv) disponibilizado no Kaggle.

## Descrição da Aplicação
A aplicação foi desenvolvida utilizando a linguagem Python e o framework FastAPI. O modelo de Machine Learning foi desenvolvido utilizando a biblioteca Scikit-Learn. A aplicação foi contêinerizada utilizando o Docker e o deploy em cloud não pode ser realizado devido a problemas correlatos ao Router 53 (AWS). 
Aplicando o modelo GradientBoostingClassifier (GBC) ao dataset, foi obtido uma precisão de 0.95. O modelo foi salvo utilizando a biblioteca Pickle e está disponível na pasta ml. A partir do modelo treinado, a aplicação web que recebe os dados de um paciente e retorna se a chance de o mesmo sofrer um AVC potencial é positiva ou negativa baseado na idade, se é hipertenso, se apresenta problemas cardíacos, o tipo de trabalho, o nível médio de glicose e o IMC. 

## Como rodar a Aplicação
### Instruções para Execução Local
Para executar a aplicação, é necessário ter o Docker instalado. Após isso, basta executar os seguintes comandos:
```
docker pull cmtabr/pda-3
docker run -d -p 80:80 cmtabr/pda-3
```

[Screencast from 2023-09-10 14-25-32.webm](https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO/assets/99201276/647172f6-c231-466f-a9e9-fe3f5a270ead)


Após isso, a aplicação estará disponível em [Local Host](http://localhost:8000)

### Instruções para Execução em Nuvem
Para executar a aplicação em nuvem, devemos primeiramente nos conectar a instância EC2, configurada com o Docker, rodar os seguintes comandos:
```
docker pull cmtabr/pda-3
docker run -dp 80:8000 cmtabr/pda-3
```

E então acessar o IPV4 público da instância, lembrando de trocar o protocolo de https para http e adicionar ":80" à URL, a porta mapeada para nossa aplicação e então acessá-la.

> [!NOTE] 
> O vídeo abaixo demonstra o funcionamento da aplicação na aws e o passo a passo citado acima.

[Screencast from 2023-09-11 20-57-58.webm](https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO/assets/99201276/8f8344ba-bc05-4083-9e9f-8499d17d51ea)

## Referências
- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Docker](https://www.docker.com/)
- [AWS](https://aws.amazon.com/pt/)
- [Kaggle](https://www.kaggle.com/)
