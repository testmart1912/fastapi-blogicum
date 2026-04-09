from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository
from src.schemas.locations import LocationSchema


class GetLocationByIdUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, location_id: int) -> LocationSchema:
        with self._database.session() as session:
            location = self._repo.get_by_id(session=session, id=location_id)

        return LocationSchema.model_validate(obj=location)
