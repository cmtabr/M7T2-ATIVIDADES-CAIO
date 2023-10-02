# Ponderada 4 - M7T2 

# Objetivo 
Essa atividade tem como objetivo avaliar a capacidade do aluno de implementar uma solução de visualização de dados utilizando o conhecimento adquirido nas últimas semanas

# Descrição
Para tal foram utilizadas as tecnologias:
| Tecnologia    | Foco       |
| ------------- | ---------- |
| AWS RDS       | Cloud (Banco de Dados Relacional)     |
| AWS EC2       | Cloud (Máquina Virtual)     |
| Streamlit     | Dashboard  |
| Python        | Backend    |

# Como executar
Clonando o repositorio em duas máquinas virtuais EC2 na AWS, uma para o backend e outra para o frontend, e executando o comando abaixo para rodar o frontend:
```
git clone https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO.git
cd M7T2-ATIVIDADES-CAIO/PONDERADA-4-PROG/frontend
sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8501
pip install -r requirements.txt
sudo iptables -I INPUT -p tcp --dport 8501 -j ACCEPT
streamlit run app.py
```
É possível acessar o dashboard através do link: http://44.220.1.246:8501/

Para rodar o backend, é necessário executar o comando abaixo:
```
git clone https://github.com/cmtabr/M7T2-ATIVIDADES-CAIO.git
cd M7T2-ATIVIDADES-CAIO/PONDERADA-4-PROG/backend
sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
pip install -r requirements.txt
uvicorn app:app --host=0.0.0.0 --port=8000
```
É possível acessar o backend através do link: http://18.215.123.203:8000/docs

Além disto é necessário criar um RDS na AWS e configurar o arquivo .env na pasta backend com as credenciais do banco de dados.

Ainda sim cabe dizer que é necessário configurar o grupo de segurança com as seguintes regras:


# Resultado
Dito isso, segue o resultado final: