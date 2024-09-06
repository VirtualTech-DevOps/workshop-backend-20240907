from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., example="一眼レフカメラ", description="商品名")
    price: int = Field(..., example=1000, description="価格")
    # ここに送料を追加


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
