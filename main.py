from fastapi import FastAPI

from src.api import api

app = FastAPI(title='MyAPI', version='0.0.0')

app.include_router(api.routeur, prefix='/api')
