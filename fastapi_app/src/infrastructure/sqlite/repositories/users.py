from sqlalchemy.orm import Session

from src.infrastructure.sqlite.repositories.base import BaseRepository
from src.infrastructure.sqlite.models.users import User
from src.core.exceptions.domain_exceptions import UserNotFoundByIdException
from src.core.exceptions.domain_exceptions import UserNotFoundByLoginException


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, UserNotFoundByIdException)

    def get_by_username(self, session: Session, username: str) -> User:
        user = (
            session.query(self._model)
            .where(self._model.username == username)
            .scalar()
        )
        if not user:
            raise UserNotFoundByLoginException(username)
        return user
