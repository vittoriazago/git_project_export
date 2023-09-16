from fastapi import FastAPI

from dotenv import load_dotenv
from app.config.api_config import configure_fast_api

app = FastAPI()

load_dotenv(verbose=True)
configure_fast_api(app)


@app.get("/")
async def root():
    return {"message": "Hello World"}
