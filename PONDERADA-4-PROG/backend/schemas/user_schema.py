from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str 
    email: str 
    password: str 

    class Config():
        json_schema_extra = {
            "example": {
                "name": "Teste",
                "email": "teste@teste.com",
                "password": "teste"
            }
        }

class UserLogin(BaseModel):
    name: str 
    password: str 
    class Config():
        json_schema_extra = {
            "example": {
                "name": "Teste",
                "password": "teste"
            }
        }
