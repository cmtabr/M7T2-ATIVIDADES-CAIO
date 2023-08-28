from pydantic import BaseModel, EmailStr 

class User(BaseModel):
    """
    Essa classe define o modelo de dados para um usuário.
    """
    name: str 
    email: EmailStr 
    password: str 
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Teste",
                "email": "teste@mail.com",
                "password": "123"
            }
        }