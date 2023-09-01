# Avaliacoes-M7-Inteli
Avaliações do Módulo 7

Para executar o projeto pelo compose, basta acessar clonar este repositório, acessar sua pasta raíz com uma IDE ou prompt de preferência e rodar o comando abaixo, com o docker desktop aberto, de preferência:

```
docker compose up -d --build 
```

# Explicação: 
Foi utilziado um dockerfile para o servidor do frontend e para a API do backend, de modo que ambos containers pudessem ser construídos através da imagem base contida no dockerfile. 

Para o docker compose foi criada uma dependência do front em relação a API, sendo que o front só é iniciado quando a build do container do backend (FASTAPI) está realizada, utilizando a tag depends-on. Desta forma é possível iniciar ambas as aplicações com o comando acima. 
Outrossim cabe ressaltar que é feita a exposição das portas padrão tanto do Node quando do FastAPI, de modo que possamos acessá-las facilmente. Além disto o container do frontend é reiniciado até que o container da api estiver pronto, já o container da API só reinicia quando há falhas.
