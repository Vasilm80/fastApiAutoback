from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers
from Auth.auth import auth_backend

from Auth.manager import get_user_manager
from Auth.shemas import UserRead, UserCreate
from models.models import av_by_user

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


fastapi_users = FastAPIUsers[av_by_user, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: av_by_user = Depends(current_user)):
    return user


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"