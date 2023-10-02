# Importing libs
from fastapi import FastAPI, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import insert, select, update, delete, ExceptionContext
import pickle
import json

auth2schema = OAuth2PasswordBearer(tokenUrl="token")

# Local packages
from config.db import conn, engine, base
from models import user, predicted
from schemas import user_schema, predicted_schema
from auth.jwt_handler import signJWT, decodeJWT
from auth.jwt_bearer import jwtBearer

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    try: 
        print("Starting connection")
        base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        print("Error creating tables")
        raise e
    finally:
        print("Startup finished")

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.post('/login')
async def login(data: user_schema.UserLogin, response: Response):
    print(data.name, data.password)
    query = select(user.UserTable).where(user.UserTable.name == data.name, user.UserTable.password == data.password)
    try:
        result = conn.execute(query).first()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            token = signJWT(str(data.name))

            print(f'Esse é o token: {token}')
            
            response = JSONResponse(content={"message": "Login successful"}, status_code=200)
            response.set_cookie(key="token", value=token, httponly=True)

        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post('/register')
async def register(data: user_schema.UserCreate):
    print(data)
    try:
        verify = select(user.UserTable).where(user.UserTable.name == data.name, user.UserTable.email == data.email)
        if conn.execute(verify).fetchone() is not None:
            print("User already exists")
            raise HTTPException(status_code=409, detail="User already exists")
        else:
            query = insert(user.UserTable).values(name=data.name, password=data.password, email=data.email)
            conn.execute(query)
            conn.commit()
            raise HTTPException(status_code=201, detail="User created")
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
    finally:
        conn.close()
    
@app.post('/predict')
async def predict(data: predicted_schema.PredictModel):
    try:
        print(data)
        print(f'Token: {data.token}')
        input = [[data.age, data.hypertension, data.heart_disease, data.work_type, data.avg_glucose_level, data.bmi]]
        print(f'Input: {input}')
        decoded = decodeJWT(data.token)
        decoded = decoded['sub']
        print(f'Decoded: {decoded}')
        userId = conn.execute(select(user.UserTable.userId).where(user.UserTable.name == decoded)).fetchall()[0][0]
        print(f'UserId: {userId}')
        model = pickle.load(open('./ml/model.pkl', 'rb'))
        evaluate = model.predict_proba(input)[0]
        prob_classe_1 = evaluate[1]
        threshold = 0.7 
        prediction = "Positivo" if prob_classe_1 >= threshold else "Negativo"
        print(prediction)
        query = insert(predicted.PredictTable).values(age=data.age, hypertension=data.hypertension, heart_disease=data.heart_disease, work_type=data.work_type, avg_glucose_level=data.avg_glucose_level, bmi=data.bmi, predicted=prediction, userId=userId)
        conn.execute(query)
        conn.commit()
        return {"message": "Prediction successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()

@app.get('/embed-data')
async def embed_data():
    query = select(predicted.PredictTable).where(predicted.PredictTable.userId == 2)
    try:
        result = conn.execute(query).fetchall()
        print(result)
        # Convert the result to a list of dictionaries
        data_list = [list(row) for row in result]

        return data_list
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
    finally:
        conn.close()