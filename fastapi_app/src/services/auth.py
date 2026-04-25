import logging
from typing import Annotated

from fastapi import Depends
from jose import JWTError, jwt

from src.core.exceptions.auth_exceptions import CredentialsException
from src.core.exceptions.database_exceptions import EntityNotFoundException
from src.schemas.users import UserSchema
from src.resources.auth import oauth2_scheme
from src.infrastructure.sqlite.database import database as sqlite_database
from src.infrastructure.sqlite.database import Database
from src.infrastructure.sqlite.repositories.users import UserRepository
from src.core.config import settings

logger = logging.getLogger(__name__)


class AuthService:
    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        _AUTH_EXCEPTION_MESSAGE = 'Unable to verify authorization data'
        _database: Database = sqlite_database
        _repo: UserRepository = UserRepository()

        try:
            payload = jwt.decode(
                token=token,
                key=settings.SECRET_AUTH_KEY.get_secret_value(),
                algorithms=[settings.AUTH_ALGORITHM]
            )
            username = payload.get('sub')
            if username is None:
                logger.error("Access attempt with invalid token (missing username)")
                raise CredentialsException(detail=_AUTH_EXCEPTION_MESSAGE)
        except JWTError as e:
            logger.error(f"Access attempt with invalid JWT token {str(e)}")
            raise CredentialsException(detail=_AUTH_EXCEPTION_MESSAGE)

        try:
            with _database.session() as session:
                user = _repo.get_by_username_or_raise(session=session, username=username)
        except EntityNotFoundException:
            logger.error(f"Access attempt with a non-existent user token - {username}")
            raise CredentialsException(detail=_AUTH_EXCEPTION_MESSAGE)

        return UserSchema.model_validate(obj=user)
