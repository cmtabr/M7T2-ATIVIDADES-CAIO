# Avaliacoes-M7-Inteli
Avaliações do Módulo 7

Para executar o projeto pelo compose, basta acessar clonar este repositório, acessar sua pasta raíz com uma IDE ou prompt de preferência e rodar o comando abaixo, com o docker desktop aberto, de preferência:

```
docker compose up -d --build 
```

# Explicação: 
Dockerfile FrontEnd: 
Utilizamos uma imagem do node, criamos um diretório para a imagem, definimos este como diretório corrente
```
FROM node:20-buster-slim

RUN mkdir /frontend 

WORKDIR /frontend
```
Copiamos os pacotes no packege.json para este diretório criado, instalamos estes pacotes e copiamos os arquivos restantes na raíz do diretório frontend para o diretório da imagem
```
COPY package.json /frontend

RUN npm install

COPY . .
```
Definimos a porta de exposição do servidor e rodamos este servidor através do comando na última linha
```
EXPOSE 3000 

CMD node server.js
```

Dockerfile BackEnd
Utilizamos uma imagem do python, criamos um diretório para a imagem, definimos este como diretório corrente
```
FROM python:3.11-slim-buster

RUN mkdir backend

WORKDIR /backend 
```
Copamos os requirementes para este diretório criado, instalamos estes pacotes e copiamos os arquivos restantes na raíz do diretório backend para o diretório da imagem e atualizamos o pip 
```
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
```
Copiamos os arquivos restantes no diretório raíz para o diretório da imagem e definimos a porta de exposição do servidor e rodamos este servidor através do comando na última linha
```
COPY . . 

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5000"]
```


Foi utilziado um dockerfile para o servidor do frontend e para a API do backend, de modo que ambos containers pudessem ser construídos através da imagem base contida no dockerfile. 

Para o docker compose foi criada uma dependência do front em relação a API, sendo que o front só é iniciado quando a build do container do backend (FASTAPI) está realizada, utilizando a tag depends-on. Desta forma é possível iniciar ambas as aplicações com o comando acima. 
Outrossim cabe ressaltar que é feita a exposição das portas padrão tanto do Node quando do FastAPI, de modo que possamos acessá-las facilmente. Além disto o container do frontend é reiniciado até que o container da api estiver pronto, já o container da API só reinicia quando há falhas.
