from datetime import datetime

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository
from src.schemas.locations import LocationSchema, LocationCreateUpdateSchema
from src.core.exceptions.database_exceptions import LocationNameConflictException
from src.core.exceptions.domain_exceptions import LocationNameAlreadyExistsException


class CreateLocationUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, dto: LocationCreateUpdateSchema) -> LocationSchema:
        with self._database.session() as session:
            try:
                location = self._repo.create(
                    session=session,
                    name=dto.name,
                    is_published=dto.is_published,
                    created_at=datetime.now(),
                )
            except LocationNameConflictException:
                raise LocationNameAlreadyExistsException(dto.name)

        return LocationSchema.model_validate(obj=location)
