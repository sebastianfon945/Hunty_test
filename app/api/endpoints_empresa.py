
# from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException

# app = APIRouter(responses={})
router = APIRouter()


@router.get("/create")
def create_object():
    return {"op": "create_object"}


@router.get("/read")
def read_object():
    return {"op": "read_object"}


@router.get("/update")
def update_object():
    return {"op": "update_object"}


@router.get("/delete")
def delete_object():
    return {"op": "delete_object"}
