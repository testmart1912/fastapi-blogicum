import logging

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository
from src.schemas.locations import LocationSchema, LocationCreateUpdateSchema
from src.core.exceptions.domain_exceptions import ForbiddenActionException

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
        with self._database.session() as session:
            location = self._repo.update(
                session=session,
                id=location_id,
                name=dto.name,
                is_published=dto.is_published
            )

        return LocationSchema.model_validate(obj=location)
