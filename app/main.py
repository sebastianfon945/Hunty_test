from fastapi import FastAPI
from api.endpoints_usuario import router as router_usuario
from api.endpoints_vacante import router as router_vacante
from api.endpoints_empresa import router as router_empresa
from db.db import client
from models.vacante import Vacante


app = FastAPI()
connect_db = client
app.include_router(router_usuario)
app.include_router(router_vacante)
app.include_router(router_empresa)
# print(connect_db)
