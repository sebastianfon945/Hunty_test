
# from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from typing import Union
from pydantic import BaseModel
from .services import insert_vacante, get_vacante


# app = APIRouter(responses={})
router = APIRouter()


class Item(BaseModel):

    position_name: str
    company_name: str
    salary: int
    currency: str
    vacancy_link: str
    required_skills: list[dict]


@router.post("/create_vacante")
def create_object(item: Item):

    insert_response, code, message = insert_vacante(item)
    if not insert_response:
        raise HTTPException(status_code=code, detail=message)
    raise HTTPException(status_code=code, detail=message)


@router.get("/read_vacante")
def read_object():
    get_response = get_vacante([])
    return {"op": "read_object"}


@router.get("/update_vacante")
def update_object():
    return {"op": "update_object"}


@router.get("/delete_vacante")
def delete_object():
    return {"op": "delete_object"}
