from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from sqlalchemy import select

import api.models.item as item_model
import api.schemas.item as item_schema


def create_item(db: Session, item: item_schema.ItemCreate) -> item_model.Item:
    db_item = item_model.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session) -> list[tuple[int, str, int]]:
    return db.query(item_model.Item).all()


def get_item(db: Session, item_id: int) -> item_model.Item:
    return db.query(item_model.Item).filter(item_model.Item.id == item_id).first()


def update_item(
    db: Session,
    item: item_schema.ItemCreate,
    original: item_model.Item,
) -> item_model.Item:
    original.name = item.name
    original.price = item.price
    # ここに送料を追加
    db.commit()
    db.refresh(original)
    return original


def delete_item(db: Session, item: item_model.Item) -> None:
    db.delete(item)
    db.commit()
