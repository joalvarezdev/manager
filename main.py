from fastapi import FastAPI
from controller.Routes import routes
from config.configuration import get_security_config

app = FastAPI()


@app.get("/")
async def home():
    return get_security_config()


app.include_router(routes)
