from fastapi import FastAPI

from api.routers import item

app = FastAPI(
    title="ワークショップAPI",
    description="ワークショップで使用するAPIです。",
    version="0.0.1",
)
app.include_router(item.router, tags=["item"])


@app.get("/")
def hello():
    return {"message": "Hello World"}
