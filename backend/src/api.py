from fastapi import FastAPI

from backend.src.connector import RedisConnector
from backend.src.router import router as main_router


app = FastAPI()
_ = RedisConnector().connect(host="redis", port=6379)

app.include_router(main_router, prefix="", tags=["Main router"])
