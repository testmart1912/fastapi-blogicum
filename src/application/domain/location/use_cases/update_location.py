import logging

from application.infrastructure.database.database import database
from application.infrastructure.database.repositories.locations import LocationRepository
from application.schemas.locations import LocationSchema, LocationCreateUpdateSchema
from application.core.exceptions.domain_exceptions import ForbiddenActionException

logger = logging.getLogger(__name__)


class UpdateLocationUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, location_id: int, dto: LocationCreateUpdateSchema, is_superuser: bool = False) -> LocationSchema:
        if not is_superuser:
            error = ForbiddenActionException()
            logger.error(f'Attempting to update a location {location_id} without superuser rights')
            raise error
        async with self._database.session() as session:
            location = await self._repo.update(
                session=session,
                id=location_id,
                name=dto.name,
                is_published=dto.is_published
            )

        return LocationSchema.model_validate(obj=location)
