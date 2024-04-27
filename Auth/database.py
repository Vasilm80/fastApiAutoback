from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from models.models import Base, av_by_user




DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# class User(SQLAlchemyBaseUserTable[int], Base):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=True)
#     phone: Mapped[str]
#     hashed_password: Mapped[str]
#     email: Mapped[str] = mapped_column(
#         String(length=320), index=True, nullable=True,
#     )
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
#     is_superuser: Mapped[bool] = mapped_column(
#         Boolean, default=False, nullable=False
#     )
#     is_verified: Mapped[bool] = mapped_column(
#         Boolean, default=False, nullable=False
#     )




engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, av_by_user)
