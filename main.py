import os
import uvicorn
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api_router import router

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"),
                port=int(os.getenv("PORT")), 
                reload=os.getenv("RELOAD"))