
# from fastapi import FastAPI
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from .services_vacante import insert_vacante, get_vacante, delete_vacante, update_vacante


# app = APIRouter(responses={})
router = APIRouter()


class ItemCreate(BaseModel):

    position_name: str
    company_name: str
    salary: int
    currency: str
    vacancy_link: str
    required_skills: list[dict]


class ItemDelete(BaseModel):

    position_name: str
    company_name: str


@router.post("/create_vacante")
def create_object(item: ItemCreate):

    insert_response, code, message = insert_vacante(item)
    if not insert_response:
        raise HTTPException(status_code=code, detail=message)
    raise HTTPException(status_code=code, detail=message)


@router.get("/read_vacante")
def read_object():
    get_response = get_vacante([])
    return {"op": "read_object"}


@router.post("/update_vacante")
async def update_object(item: Request):
    item = await item.json()
    import pdb; pdb.set_trace()
    insert_response, code, message = update_vacante(item)
    return {"op": "update_object"}


@router.delete("/delete_vacante")
def delete_object(item: ItemDelete):
    # Eliminar por vacante y empresa
    insert_response, code, message = delete_vacante(item)
    if not insert_response:
        raise HTTPException(status_code=code, detail=message)
    raise HTTPException(status_code=code, detail=message)
