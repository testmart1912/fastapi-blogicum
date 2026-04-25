from sqlalchemy.orm import Session

from src.infrastructure.sqlite.repositories.base import BaseRepository
from src.infrastructure.sqlite.models.users import User
from src.core.exceptions.domain_exceptions import UserNotFoundByIdException
from src.core.exceptions.domain_exceptions import UserNotFoundByLoginException


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, UserNotFoundByIdException)

    def get_by_username(self, session: Session, username: str) -> User | None:
        return (
            session.query(self._model)
            .where(self._model.username == username)
            .scalar()
        )

    def get_by_username_or_raise(self, session: Session, username: str) -> User:
        user = self.get_by_username(session=session, username=username)
        if not user:
            raise UserNotFoundByLoginException(username)
        return user
