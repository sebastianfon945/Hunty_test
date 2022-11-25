
# from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException

# app = APIRouter(responses={})
router = APIRouter()


@router.get("/create_empresa")
def create_object():
    return {"op": "create_object"}


@router.get("/read_empresa")
def read_object():
    return {"op": "read_object"}


@router.get("/update_empresa")
def update_object():
    return {"op": "update_object"}


@router.get("/delete_empresa")
def delete_object():
    return {"op": "delete_object"}
