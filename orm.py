from pydantic import json
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload


from db import session_factory
from models.models import av_by_user, Car, City


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
def get_car_ad(id: int):
    with session_factory() as s:
        query = select(Car)
        res = s.execute(query.filter(Car.user_id == id))
        return res.scalars().all()

@staticmethod
def insert_user(user: dict):
    with session_factory() as s:
        query = insert(av_by_user).values(user)
        s.execute(query)
        s.commit()
    return f'Пользователь добавлен'

@staticmethod
def select_car_page(page: int=1):
    with session_factory() as s:
        query = select(Car)
        d = s.execute(query.order_by(Car.data_create.desc()))
        r = d.scalars().all()[:10*page]
        return r

@staticmethod
def insert_car(car: dict):
    with session_factory() as s:
        query = insert(Car).values(car)
        s.execute(query)
        s.commit()
        return {'statys': 'sucsess',
                'car': car,}

@staticmethod
def userlogin(name: str, password: str):

    with session_factory() as session:
        query = (select(av_by_user.name, av_by_user.password).filter())
        res_query = session.execute(query)
        query_d = dict(res_query.all())

        try:
            if query_d[f'{name}'] == password:
                query_user = (select(av_by_user.id, av_by_user.name))
                res_query_user = session.execute(query_user)
                res = dict(res_query_user.all())
                for k, v in res.items():
                    if v == name:
                        return {'status': True, 'User_id': k, 'name': v}
            else:
                return {'status':False}
        except:
            return {'status': False}

@staticmethod
def userreg(ph, n, p):
    with session_factory() as s:
        query_name = select(av_by_user.name)
        res_name = s.execute(query_name).scalars().all()
        if n in res_name:
            return {'status': False, 'mes': 'Такое имя уже есть. Придумайте другое' }
        stm = insert(av_by_user).values({'phone': ph,'name': n, 'password': p, 'hashed_password': p })
        s.execute(stm)
        s.commit()
        query_id = select(av_by_user.id).filter(av_by_user.name == n)
        k = s.execute(query_id).scalars().all()
        return {'status': True, 'User_id': k[0], 'name': n}