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
 ┃ ┗ 📂static
 ┃   ┗ 📜css
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

[Screencast from 2023-09-10 13-22-29.webm](https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO/assets/99201276/bbd8ecd3-0a62-4855-a005-9658b1976bac)

Após isso, a aplicação estará disponível em [Local Host](http://localhost:80)

### Instruções para Execução em Nuvem
Para executar a aplicação em nuvem, bastaria acessar o seguinte link: [WebApp](https://ec2-18-208-172-6.compute-1.amazonaws.com:8000). Porém, devido a problemas com o Router 53, não foi possível realizar o deploy em nuvem. 

![WARNING] 
> O vídeo abaixo contém cenas fortíssimas de não entendimento do que está acotencendo na AWS

[Screencast from 2023-09-10 13-45-02.webm](https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO/assets/99201276/cbd032d0-3109-42ce-a270-fbaf64f7b67a)

'[NOTE]
>Como foi possível visualizar, a subnet está bloqueada, não permitindo o host de um domínio, bem como seu acesso por quaisquer outros meios, em decorrência da falta de permissionamento na ferramenta Route 53.
>Não pude realizar esta parte da atividade, ainda que quisesse, devido à este inconveniente, tentei por outros métodos, como o S3, ECS e LightSail, mas nada adiantou muito.


## Referências
- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Docker](https://www.docker.com/)
- [AWS](https://aws.amazon.com/pt/)
- [Kaggle](https://www.kaggle.com/)
