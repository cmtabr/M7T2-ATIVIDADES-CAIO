from fastapi import FastAPI, Request, HTTPException, Depends, Form, Header
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy import insert, select, update, delete, ExceptionContext
import time

# Importing database config
from .config.db import conn

# Importing schemas
from .schemas.index import User, Todo, UserLogin

# Importing models
from .models.index import UserTable, TodoTable

# Importing auth 
from .auth.jwt_bearer import jwtBearer
from .auth.jwt_handler import signJWT, decodeJWT, token_response

app = FastAPI()

app.mount("/static", StaticFiles(directory="api/static", html=True), name="static")

templates = Jinja2Templates(directory="api/templates")

# Páginas do site
@app.route('/')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.route('/todo', methods=['GET', 'POST'])
async def todo(request: Request, token: str = Header(...)):
    try:
        payload = decodeJWT(token)
        user_id = payload["sub"]
        return templates.TemplateResponse("todo.html", {"request": request, "user_id": user_id})
    
    except Exception as e:
        raise HTTPException(status_code=403, detail="Unauthorized")

@app.route('/user', methods=['GET', 'POST'])
async def user_page(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})


@app.post('/api/login')
async def login(username: str = Form(...), password: str = Form(...)):
    """
    This function performs user login.
    """
    print(username, password)
    try:
        query = select(UserTable).where(UserTable.name == username)
        result = conn.execute(query).first()
        if result:
            print(result)
        else:
            raise HTTPException(status_code=400, detail="User does not exist.")
        user_id, db_username, db_email, db_password = (result)
        if db_password != password:
            raise HTTPException(status_code=400, detail="Incorrect password.")
        token = signJWT(user_id)
        print(f'Token: {token}')
        redirect_url = "/todo"
        response = JSONResponse(content={"token": token, "redirect_url": redirect_url})
        
        response.set_cookie(key="jwt_token", value=token, httponly=True)
        return RedirectResponse(url=redirect_url), token
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/api/create_todo')
async def create_todo(
    task: str = Form(...),
    description: str = Form(...),
    status: int = Form(...),
    priority: int = Form(...),
    user_id: int = Form(...),  
    token: str = Header(...)
):
    """
    This function inserts a todo for a user into the database
    """
    try:
        # Decode the token to verify the user's identity
        payload = decodeJWT(token)
        if payload["sub"] != user_id:  # Ensure the user_id matches the token
            raise HTTPException(status_code=403, detail="Forbidden")
        
        # Create a new ToDo instance
        new_todo = TodoTable.insert().values(
            task=task,
            description=description,
            status=status,
            priority=priority,
            userId=user_id
        )
        result = conn.execute(new_todo)
        
        return JSONResponse(content={"message": "ToDo created successfully"})
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))