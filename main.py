import opszero_rustypy

from mangum import Mangum

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def cats(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dogs/{id}")
def dog(id):
    return "Dog"


@app.get("/rust")
def rust():
    return opszero_rustypy.sum_as_string(1, 2)


@app.get("/health")
def health():
    return {"status": "Success"}


@app.get("/rust")
def health():
    return {"status": "Success"}


handler = Mangum(app)
