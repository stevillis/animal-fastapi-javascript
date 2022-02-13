from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from api import animal_router
from data import AnimalList

animal_list = AnimalList()
app = FastAPI()

origins = [
    'http://127.0.0.1:5500',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', tags=['main'], response_class=HTMLResponse)
def main():
    """
    View that shows description about the Animal API
    :return: A link to the API instructions
    """
    return """<a href="http://localhost:8000/docs">API instructions</a>"""


app.include_router(animal_router, prefix='/animais', tags=['animais'])
