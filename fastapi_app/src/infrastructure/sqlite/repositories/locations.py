from src.infrastructure.sqlite.repositories.base import BaseRepository
from src.infrastructure.sqlite.models.locations import Location


class LocationRepository(BaseRepository[Location]):
    def __init__(self):
        super().__init__(Location)
