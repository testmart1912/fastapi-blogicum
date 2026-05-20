import logging

from application.infrastructure.sqlite.database import database
from application.infrastructure.sqlite.repositories.users import UserRepository
from application.schemas.users import UserSchema
from application.core.exceptions.database_exceptions import UserNotFoundException
from application.core.exceptions.domain_exceptions import UserNotFoundByLoginException

logger = logging.getLogger(__name__)


class GetUserByUsernameUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username: str) -> UserSchema:
        try:
            with self._database.session() as session:
                user = self._repo.get_by_username_or_raise(
                    session=session, username=username
                )
        except UserNotFoundException:
            error = UserNotFoundByLoginException(username=username)
            logger.error(f"User {username} not found")
            raise error

        return UserSchema.model_validate(obj=user)
