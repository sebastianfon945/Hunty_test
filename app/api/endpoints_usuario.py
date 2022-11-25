
# from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from .services_usuario import insert_usuario, get_usuario, delete_usuario, update_usuario


# app = APIRouter(responses={})
router = APIRouter()


class ItemCreateUser(BaseModel):

    first_name: str
    last_name: str
    email: str
    years_previous_experience: int
    skills: list[dict]


class ItemDelete(BaseModel):

    first_name: str
    last_name: str


@router.post("/create_usuario")
def create_object(item: ItemCreateUser):

    insert_response, code, message = insert_usuario(item)
    if not insert_response:
        raise HTTPException(status_code=code, detail=message)
    raise HTTPException(status_code=code, detail=message)


@router.get("/read_usuario")
def read_object():
    get_response = get_usuario([])
    return {"op": "read_object"}


@router.post("/update_usuario")
async def update_object(item: Request):
    item = await item.json()
    insert_response, code, message = update_usuario(item)
    return {"op": "update_object"}


@router.delete("/delete_usuario")
def delete_object(item: ItemDelete):
    # Eliminar por vacante y empresa
    insert_response, code, message = delete_usuario(item)
    if not insert_response:
        raise HTTPException(status_code=code, detail=message)
    raise HTTPException(status_code=code, detail=message)
