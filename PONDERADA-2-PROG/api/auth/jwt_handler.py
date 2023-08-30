# É o responsável por assinar, decodificar, codificar e retornar os JWTs.
# Cada JWT deve possuir um tempo de vida, assim a biblioteca time é utilizada para criar esse controle de tempo
import time
import jwt
import os
# Realiza a leitura de arquivos de ambiente
from decouple import config 

JWT_SECRET = config('SECRET')
JWT_ALGORITHM = config('ALGORITHM')

# Função que gera um JWT
def token_response(token:str):
    return {
        "access token" : token
    }

# Função que assina um JWT
def signJWT(userId : int):
    payload = { 
        "sub" : userId,
        "expires" : time.time() + 3000 
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)
    return token_response(token)

# Função que decodifica um JWT
def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        if decode_token["expires"] >= time.time():
            print(f'Token válido: {decode_token}')
            return decode_token
    except jwt.ExpiredSignatureError:
        return f'Token expirado: {decode_token}'
    except jwt.DecodeError:
        return f'Erro no decode: {decode_token}'