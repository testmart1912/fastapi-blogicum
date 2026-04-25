import logging

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository
from src.core.exceptions.domain_exceptions import ForbiddenActionException

logger = logging.getLogger(__name__)


class DeleteLocationUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, location_id: int, is_superuser: bool = False) -> bool:
        if not is_superuser:
            error = ForbiddenActionException()
            logger.error(f'Attempting to delete a location {location_id} without superuser rights')
            raise error
        with self._database.session() as session:
            self._repo.delete(session=session, id=location_id)

        return True
