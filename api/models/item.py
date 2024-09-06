from sqlalchemy import Column, Integer, String
from api.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    price = Column(Integer)
    # ここに送料を追加
