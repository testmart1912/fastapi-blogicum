from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository
from src.schemas.locations import LocationSchema, LocationCreateUpdateSchema


class UpdateLocationUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, location_id: int, dto: LocationCreateUpdateSchema) -> LocationSchema:
        with self._database.session() as session:
            location = self._repo.update(
                session=session,
                id=location_id,
                name=dto.name,
                is_published=dto.is_published,
            )

        return LocationSchema.model_validate(obj=location)
