from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.db import get_db

import api.schemas.item as item_schema
import api.cruds.item as item_crud

router = APIRouter()


@router.post("/item", response_model=item_schema.Item)
def create_item(
    item: item_schema.ItemCreate,
    db: Session = Depends(get_db),
):
    return item_crud.create_item(db, item)


@router.get("/items", response_model=list[item_schema.Item])
def get_items(db: Session = Depends(get_db)):
    return item_crud.get_items(db)


@router.get("/item/{item_id}", response_model=item_schema.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.put("/item/{item_id}", response_model=item_schema.Item)
def update_item(
    item_id: int,
    item_body: item_schema.ItemCreate,
    db: Session = Depends(get_db),
):
    item = item_crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item_crud.update_item(db, item_body, original=item)


@router.delete("/item/{item_id}", response_model=None)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item_crud.delete_item(db, item)
