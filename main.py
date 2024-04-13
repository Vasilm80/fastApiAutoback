from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from orm import select_car
from router.router import router

app = FastAPI(
    title='Autobuy'
)

origins = [
    "http://localhost:3000",
    "127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.get('/')
def get_user():
    return 'Hello, word'


app.include_router(router)
