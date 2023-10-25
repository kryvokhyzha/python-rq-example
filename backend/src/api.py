from fastapi import FastAPI

from backend.src.redis_connector import RedisConnector
from backend.src.router import router as main_router


app = FastAPI()
_ = (
    RedisConnector()
    .update_connection(host="redis", port=6379)
    .update_queue("high")
    .update_queue("default")
    .update_queue("low")
)

app.include_router(main_router, prefix="", tags=["Main router"])
