from datetime import datetime

from sqlalchemy import MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import Annotated

from sqlalchemy.testing.pickleable import User


class Base(DeclarativeBase):
    metadata = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]

class av_by_user(Base):
    __tablename__ = 'av_by_user'
    id: Mapped[intpk]
    name: Mapped[str]
    phone: Mapped[str]
    photo: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str]



class City(Base):
    __tablename__ = 'av_by_city'
    id: Mapped[intpk]
    name: Mapped[str]
    region: Mapped[str]



class Car(Base):
    __tablename__ = 'av_by_car'
    id: Mapped[intpk]
    mark_car: Mapped[str]
    model_car: Mapped[str]
    generation: Mapped[str]
    body: Mapped[str]
    motor: Mapped[str]
    transmission: Mapped[str]
    drive: Mapped[str]
    year: Mapped[int]
    price: Mapped[int]
    volume: Mapped[str]
    photo: Mapped[str]
    vin: Mapped[str] = mapped_column(nullable=True)
    data_create: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    mileage: Mapped[int]
    color: Mapped[str]
    condition: Mapped[str]
    description: Mapped[str]
    exchange: Mapped[str]
    options: Mapped[str]
    city_id_id: Mapped[int] = mapped_column(ForeignKey('City.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('av_by_user.id'))


