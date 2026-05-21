from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.infrastructure.database.repositories.base import BaseRepository
from application.infrastructure.database.models.users import User
from application.core.exceptions.domain_exceptions import UserNotFoundByIdException
from application.core.exceptions.domain_exceptions import UserNotFoundByLoginException


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, UserNotFoundByIdException)

    async def get_by_username_or_raise(self, session: AsyncSession, username: str) -> User:
        query = select(self._model).where(self._model.username == username)
        user = await session.scalar(query)
        if not user:
            raise UserNotFoundByLoginException(username)
        return user

    async def update_user(self, session: AsyncSession, user_id: int, update_data: dict) -> User:
        query = select(self._model).where(self._model.id == user_id)
        user = await session.scalar(query)
        if not user:
            raise UserNotFoundByLoginException(user.username)

        for key, value in update_data.items():
            if value is not None:
                setattr(user, key, value)

        return user
