# Importing libs
from fastapi import FastAPI, HTTPException, status, Depends, Request, Response, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import insert, select, update, delete, ExceptionContext
from sqlalchemy.exc import NoResultFound, TimeoutError

# Local packages
from config.db import conn, metadata, engine, base
from models import user, predicted  

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
        print("Creating tables")
        base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        print("Error creating tables")
        raise e
    finally:
        print("Tables created")

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.post('/login')
async def login(user, password):
    try:
        query = conn.execute(f"SELECT * FROM user WHERE user = '{user}' AND password = '{password}'")
        result = query.fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
