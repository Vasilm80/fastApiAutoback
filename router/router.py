from fastapi import APIRouter
from orm import select_user, select_city, select_car, get_car_id, insert_user, select_car_page

router = APIRouter(
    prefix='/api',
    tags=['API']
)

@router.get('/city/')
def get_city():
    c = select_city()
    return c

@router.get('/car/')
def get_car():
    car = select_car()
    return car

@router.get('/car/{id}')
def get_car(id:int):
    car = get_car_id(id)
    return car

@router.get('/user/')
def get_user():
    user = select_user()
    return user

@router.get('/carpage/{page}')
def get_car(page:int =1):
    car = select_car_page(page)
    return car

@router.post('/user/')
def create_user(user:dict):
    r = insert_user(user)
    return r
