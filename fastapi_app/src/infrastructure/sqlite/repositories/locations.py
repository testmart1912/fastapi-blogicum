from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.infrastructure.sqlite.repositories.base import BaseRepository
from src.infrastructure.sqlite.models.locations import Location
from src.core.exceptions.domain_exceptions import LocationNotFoundByIdException
from src.core.exceptions.database_exceptions import LocationNameConflictException


class LocationRepository(BaseRepository[Location]):
    def __init__(self):
        super().__init__(Location, LocationNotFoundByIdException)

    def create(self, session: Session, **kwargs) -> Location:
        try:
            return super().create(session=session, **kwargs)
        except IntegrityError:
            raise LocationNameConflictException()
