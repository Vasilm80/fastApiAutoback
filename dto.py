from pydantic import BaseModel

class UserAuthDTO(BaseModel):
    name: str
    password: str

class CarDTO(BaseModel):
    mark_car: str
    model_car: str
    generation: str
    body: str
    motor: str
    transmission: str
    drive: str
    year: int
    price: int
    volume: str
    photo: str
    vin: str | None = None
    mileage: int
    color: str
    condition: str
    description: str
    exchange: str
    options: str | None = None
    city_id_id: int
    user_id: int

class UserFavDTO(BaseModel):
    car_id: int
    user_id: int

class UserRegDTO(BaseModel):
    phone: str
    name: str
    password: str