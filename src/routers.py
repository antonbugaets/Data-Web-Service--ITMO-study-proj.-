from cgitb import html
from typing import Optional
from fastapi import APIRouter
from contracts import Item

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/users/")
async def read_user(user_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": user_id, "q": q}
    return {"item_id": user_id}


@router.post("/items/")
async def create_item(item: Item): 
    return item.name



    
