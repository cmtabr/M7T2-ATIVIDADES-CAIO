from fastapi import FastAPI, Request, Response, status, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, age: int = Form(...), hypertension: int = Form(...), heart_disease: int = Form(...), work_type: int = Form(...), avg_glucose_level: float = Form(...), bmi: float = Form(...)):
    try:
        input_data = [[
            age,
            hypertension,
            heart_disease,
            work_type,
            avg_glucose_level,
            bmi
        ]]
        model = pickle.load(open('./ml/model.pkl', 'rb'))
        prediction = model.predict_proba(input_data)[0]
        prob_classe_1 = prediction[1]
        threshold = 0.5 
        if prob_classe_1 >= threshold:
            prediction_result = "Positivo"
        else:
            prediction_result = "Negativo"

        # Render the HTML template with the prediction result
        return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction_result})
    except Exception as e:
        return HTMLResponse(content=f"<html><body>Error: {str(e)}</body></html>", status_code=500)
    
