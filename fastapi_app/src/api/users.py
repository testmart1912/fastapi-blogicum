from fastapi import APIRouter, status, Depends

from src.schemas.users import UserSchema
from src.domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase

from src.api.depends import get_get_user_by_username_use_case

router = APIRouter()


@router.get('/user/{username}', status_code=status.HTTP_200_OK, response_model=UserSchema)
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsernameUseCase = Depends(get_get_user_by_username_use_case),
) -> UserSchema:
    user = await use_case.execute(username=username)
    return user
