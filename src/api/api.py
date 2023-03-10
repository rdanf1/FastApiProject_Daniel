from fastapi import APIRouter

from src.api.endpoints import productWs

routeur = APIRouter()
routeur.include_router(productWs.routeur, prefix='/product',
                       tags=["Product"],
                       responses={404: {"description": "Impossible"}})

