from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str = Field(..., title="Name")
    email: str = Field(..., title="Email")
    password: str = Field(..., title="Password")

    class Config():
        json_schema_extra = {
            "example": {
                "name": "Teste",
                "email": "teste@teste.com",
                "password": "teste"
            }
        }