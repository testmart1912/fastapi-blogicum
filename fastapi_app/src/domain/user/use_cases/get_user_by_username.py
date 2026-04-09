from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.users import UserRepository
from src.schemas.users import UserSchema
from src.core.exceptions.database_exceptions import UserNotFoundException
from src.core.exceptions.domain_exceptions import UserNotFoundByLoginException


class GetUserByUsernameUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username: str) -> UserSchema:
        try:
            with self._database.session() as session:
                user = self._repo.get_by_username(
                    session=session, username=username
                )
        except UserNotFoundException:
            raise UserNotFoundByLoginException(username=username)

        return UserSchema.model_validate(obj=user)
