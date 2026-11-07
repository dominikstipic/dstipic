from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

tempatles = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
     return tempatles.TemplateResponse(request, "home.html", {"posts": []})

