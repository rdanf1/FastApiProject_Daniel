from fastapi import FastAPI

from src.api import api

app = FastAPI()

app.include_router(api.routeur, prefix='/api')
