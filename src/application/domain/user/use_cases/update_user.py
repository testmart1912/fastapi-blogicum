import logging

from application.infrastructure.sqlite.database import database
from application.infrastructure.sqlite.repositories.users import UserRepository
from application.schemas.users import UserResponseSchema, UserCreateUpdateSchema
from application.core.exceptions.domain_exceptions import (
    UserNotFoundByIdException,
    ForbiddenActionException
)
from application.resources.auth import get_password_hash

logger = logging.getLogger(__name__)


class UpdateUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(
        self,
        target_user_id: int,
        dto: UserCreateUpdateSchema,
        current_user_id: int,
        is_superuser: bool = False) -> UserResponseSchema:
        if not is_superuser and current_user_id != target_user_id:
            logger.error(f'User {current_user_id} attempted to update profile of user {target_user_id}')
            raise ForbiddenActionException()

        update_data = dto.model_dump(exclude_none=True)

        if 'password' in update_data:
            update_data['password'] = get_password_hash(update_data['password'])

        with self._database.session() as session:
            try:
                user = self._repo.update(session=session, id=target_user_id, **update_data)
                session.commit()
                session.refresh(user)
            except Exception:
                raise UserNotFoundByIdException(id=target_user_id)

        return UserResponseSchema.model_validate(obj=user)
