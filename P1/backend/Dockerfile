FROM python:3.11-slim-buster

RUN mkdir backend

WORKDIR /backend 

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5000"]