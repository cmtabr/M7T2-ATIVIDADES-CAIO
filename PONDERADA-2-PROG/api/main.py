from fastapi import FastAPI, Request, HTTPException, Depends, Form, Response    
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import insert, select, update, delete, ExceptionContext
import time, json

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
async def todo(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request})

@app.route('/user', methods=['GET', 'POST'])
def user_page(request: Request):
    jwt_token = request.cookies.get('token')
    print(f'Esse é o jwt_token: {jwt_token}')
    token = eval(jwt_token)
    print(f'Esse é o token: {token}')
    x = token.get('access token')
    payload = decodeJWT(x)
    userId = payload.get("sub")
    query=conn.execute(select(TodoTable).where(TodoTable.userId == userId))
    result = query.fetchall()
    print(f'Esse é o result: {result}')
    
    tasks = [task for task in result] 

    return templates.TemplateResponse("user.html", {"request": request, 'tasks': tasks})

@app.get('/add_new')
def add_new():
    return RedirectResponse(url='/todo', status_code=302)

@app.post('/api/delete/{id}')
async def delete_todo(id: int):
    try:
        conn.execute(delete(TodoTable).where((TodoTable.todoId == id)))
        conn.commit()
        return RedirectResponse(url='/user', status_code=302)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

@app.post('/api/update/{id}')
async def update_task(id: int, task: str = Form(...), description: str = Form(...), status: int = Form(...), priority: int = Form(...)):
    try:
        conn.execute(update(TodoTable).where(TodoTable.todoId == id).values(
            task=task,
            description=description,
            status=status,
            priority=priority
        ))
        conn.commit()
        return RedirectResponse(url='/user', status_code=302)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    
@app.post('/api/login')
async def login(username: str = Form(...), password: str = Form(...)):
    """
    This function performs user login.
    """
    print(username, password)
    try:
        query = select(UserTable).where(UserTable.name == username)
        result = conn.execute(query).first()
        
        if not result:
            raise HTTPException(status_code=400, detail="User does not exist.")
        
        user_id, db_username, db_email, db_password = result
        
        print(f'Esse é o user_id: {user_id} \r\n Essa é a resposta: {result}')

        if db_password != password:
            raise HTTPException(status_code=400, detail="Incorrect password.")
        
        token = signJWT(user_id)

        print(f'Esse é o token: {token}')
        
        redirect_url = "/todo"
        response = RedirectResponse(url=redirect_url, status_code=302)
        response.set_cookie(key="token", value=token)  

        print(f'Esse é o response: {response}')

        return response
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/api/create_todo')
async def create_todo(
    request: Request,
    task: str = Form(...),
    description: str = Form(...),
    status: int = Form(...),
    priority: int = Form(...),
    ):
    """
    This function inserts a todo for a user into the database
    """
    try:
        # Decode the token to verify the user's identity
        print(f'Esse é o request: {request}')
        jwt_token = request.cookies.get('token')
        print(f'asdasdasd : {jwt_token}')
        dict = eval(jwt_token)
        print(f'Esse é o dict: {dict}')
        x = dict.get('access token')
        print(f'Esse é o x: {x}')
        token = x
        payload = decodeJWT(token)
        userId = payload.get("sub")  # Replace with the actual key in your payload
        
        # Proceed with creating the todo
        new_todo = insert(TodoTable).values(
            task=task,
            description=description,
            status=status,
            priority=priority,
            userId=userId
        )
        conn.execute(new_todo)
        conn.commit()

        return RedirectResponse(url="/user", status_code=302)


    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))