import logging

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.users import UserRepository
from src.schemas.users import UserSchema
from src.resources.auth import verify_password
from src.core.exceptions.database_exceptions import EntityNotFoundException
from src.core.exceptions.domain_exceptions import UserNotFoundByLoginException
from src.core.exceptions.domain_exceptions import WrongPasswordException

logger = logging.getLogger(__name__)


class AuthenticateUserUseCase:
    def __init__(self) -> None:
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username: str, password: str) -> UserSchema:
        try:
            with self._database.session() as session:
                user = self._repo.get_by_username_or_raise(session=session, username=username)
        except EntityNotFoundException:
            error = UserNotFoundByLoginException(username=username)
            logger.error(f'Attempted to log in with a non-existent login {username}')
            raise error

        if not verify_password(plain_password=password, hashed_password=user.password):
            error = WrongPasswordException()
            logger.error(f'Incorrect password for user {username}')
            raise error

        return UserSchema.model_validate(obj=user)
