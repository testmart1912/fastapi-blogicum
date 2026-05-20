from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException

from application.schemas.users import UserSchema, UserCreateUpdateSchema, UserResponseSchema
from application.domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase
from application.domain.user.use_cases.update_user import UpdateUserUseCase
from application.core.exceptions.domain_exceptions import (
    UserNotFoundByLoginException,
    UserNotFoundByIdException,
    ForbiddenActionException
)
from application.api.depends import (
    get_get_user_by_username_use_case,
    get_update_user_use_case,
)
from application.schemas.base import UsernameStr
from application.services.auth import AuthService

router = APIRouter(dependencies=[Depends(AuthService.get_current_user)])


@router.get('/user/{username}', status_code=status.HTTP_200_OK, response_model=UserSchema)
async def get_user_by_username(
    username: UsernameStr,
    use_case: GetUserByUsernameUseCase = Depends(get_get_user_by_username_use_case)) -> UserSchema:
    try:
        return await use_case.execute(username=username)
    except UserNotFoundByLoginException as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=exc.get_detail())


@router.put('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
async def update_user(
    user_id: int,
    dto: UserCreateUpdateSchema,
    current_user: Annotated[UserSchema, Depends(AuthService.get_current_user)],
    use_case: UpdateUserUseCase = Depends(get_update_user_use_case)) -> UserResponseSchema:

    try:
        return await use_case.execute(
            target_user_id=user_id,
            dto=dto,
            current_user_id=current_user.id,
            is_superuser=current_user.is_superuser,
        )
    except ForbiddenActionException as exc:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=exc.get_detail())
    except UserNotFoundByIdException as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=exc.get_detail())
