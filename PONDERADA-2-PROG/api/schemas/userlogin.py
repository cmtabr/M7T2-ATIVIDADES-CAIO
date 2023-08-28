from pydantic import BaseModel, Field, EmailStr 

class UserLogin(BaseModel):
    """
    Essa classe define o modelo de dados para o login de um usuário
    """
    name: str 
    email: EmailStr 
    password: str 
    class Config:
        json_schema_extra = {
            "example": {
                "name": "teste",
                "email": "teste@mail.com",
                "password": "teste123"
            }
        }
