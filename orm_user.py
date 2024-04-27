from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from db import session_factory, async_sessino_factiory

from models.models import Favorites, Car, MessagesCar


@staticmethod
def insert_favorite(user_id: int, car_id: int):
    with session_factory() as s:
        query = insert(Favorites).values({'user_id': user_id, 'car_id': car_id})
        s.execute(query)
        s.commit()
    return f'Машина добавлена в избранное'

@staticmethod
def select_favorite(user_id: int):
    with session_factory() as s:
        query = select(Favorites).filter(Favorites.user_id == user_id).options(joinedload(Favorites.car))
        fav = s.execute(query).scalars().all()
        return fav

@staticmethod
def insert_mes(mes):
    with session_factory() as s:
        query = insert(MessagesCar).values(mes)
        s.execute(query)
        s.commit()
    return f'Сообщение отправлено'


@staticmethod
def select_message(id: int):
    with session_factory() as s:
        query = select(MessagesCar).filter(MessagesCar.user_id == id).options(joinedload(MessagesCar.carmes)).options(joinedload(MessagesCar.usermes)).order_by(MessagesCar.car_id)
        r = s.execute(query).scalars().all()
        return r

@staticmethod
def sel_mes_owner(id: int):
    with session_factory() as s:
        query = select(MessagesCar).options(joinedload(MessagesCar.carmes))
        r = s.execute(query).scalars().all()
        return r