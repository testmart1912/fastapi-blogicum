from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, Query

from src.schemas.locations import LocationSchema, LocationCreateUpdateSchema
from src.schemas.users import UserSchema
from src.domain.location.use_cases.get_location_by_id import GetLocationByIdUseCase
from src.domain.location.use_cases.create_location import CreateLocationUseCase
from src.domain.location.use_cases.update_location import UpdateLocationUseCase
from src.domain.location.use_cases.delete_location import DeleteLocationUseCase
from src.domain.location.use_cases.get_all_locations import GetAllLocationsUseCase
from src.core.exceptions.domain_exceptions import LocationNotFoundByIdException
from src.core.exceptions.domain_exceptions import LocationNameAlreadyExistsException
from src.core.exceptions.domain_exceptions import ForbiddenActionException
from src.api.depends import get_get_location_by_id_use_case, get_create_location_use_case, get_update_location_use_case, get_delete_location_use_case, get_get_all_locations_use_case
from src.services.auth import AuthService

router = APIRouter()


@router.get('/locations', status_code=status.HTTP_200_OK, response_model=List[LocationSchema])
async def get_all_locations(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    use_case: GetAllLocationsUseCase = Depends(get_get_all_locations_use_case)) -> List[LocationSchema]:
    locations = await use_case.execute(limit=limit, offset=offset)
    return locations


@router.get('/location/{location_id}', status_code=status.HTTP_200_OK, response_model=LocationSchema)
async def get_location_by_id(
    location_id: int,
    use_case: GetLocationByIdUseCase = Depends(get_get_location_by_id_use_case)) -> LocationSchema:
    try:
        location = await use_case.execute(location_id=location_id)
    except LocationNotFoundByIdException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.get_detail()
        )
    return location


@router.post('/location', status_code=status.HTTP_201_CREATED, response_model=LocationSchema)
async def create_location(
    dto: LocationCreateUpdateSchema,
    current_user: UserSchema = Depends(AuthService.get_current_user),
    use_case: CreateLocationUseCase = Depends(get_create_location_use_case)) -> LocationSchema:
    try:
        location = await use_case.execute(dto=dto, is_superuser=current_user.is_superuser)
    except LocationNameAlreadyExistsException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=exc.get_detail()
        )
    except ForbiddenActionException as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=exc.get_detail()
        )
    return location


@router.put('/location/{location_id}', status_code=status.HTTP_200_OK, response_model=LocationSchema)
async def update_location(
    location_id: int,
    dto: LocationCreateUpdateSchema,
    current_user: UserSchema = Depends(AuthService.get_current_user),
    use_case: UpdateLocationUseCase = Depends(get_update_location_use_case)) -> LocationSchema:
    try:
        location = await use_case.execute(location_id=location_id, dto=dto, is_superuser=current_user.is_superuser)
    except LocationNotFoundByIdException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.get_detail()
        )
    except ForbiddenActionException as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=exc.get_detail()
        )
    return location


@router.delete('/location/{location_id}', status_code=status.HTTP_200_OK)
async def delete_location(
    location_id: int,
    current_user: UserSchema = Depends(AuthService.get_current_user),
    use_case: DeleteLocationUseCase = Depends(get_delete_location_use_case)) -> dict:
    try:
        await use_case.execute(location_id=location_id, is_superuser=current_user.is_superuser)
    except LocationNotFoundByIdException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.get_detail()
        )
    except ForbiddenActionException as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=exc.get_detail()
        )
    return {'message': 'Location has been deleted'}
