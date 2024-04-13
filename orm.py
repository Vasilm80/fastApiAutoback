from pydantic import json
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload
from db import session_factory
from models.models import av_by_user, Car, City


# @staticmethod
# def insert_data():
#     us = User(name='Vas', phone = '293333333', password = '123')
#     with session_factory() as session:
#         session.add(us)
#         session.commit()

@staticmethod
def select_car():
    with session_factory() as s:
        car = s.execute(select(Car).order_by(Car.data_create.desc()))
        c = car.scalars().all()
        return c


@staticmethod
def select_data():
    with session_factory() as session:
        query = select(av_by_user.name)
        result = session.execute(query)
        user = result.scalars().all()
        print(f'Users: \n {user}')

@staticmethod
def select_user():
    with session_factory() as session:
        query = select(av_by_user)
        res = session.execute(query)
        return res.scalars().all()

@staticmethod
def select_city():
    with session_factory() as s:
        query = select(City)
        res = s.execute(query)
        return res.scalars().all()

@staticmethod
def get_car_id(id: int):
    with session_factory() as s:
        query = select(Car)
        res = s.execute(query.filter(Car.id == id))
        return res.scalars().first()

@staticmethod
def insert_user(user: dict):
    with session_factory() as s:
        query = insert(av_by_user).values(user)
        s.execute(query)
        s.commit()
    return f'Пользователь {user.name} добавлен'

@staticmethod
def select_car_page(page: int=1):
    with session_factory() as s:
        query = select(Car)
        d = s.execute(query.order_by(Car.data_create.desc()))
        r = d.scalars().all()[:10*page]
        return r