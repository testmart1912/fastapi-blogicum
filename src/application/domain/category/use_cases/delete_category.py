import logging

from application.infrastructure.database.database import database
from application.infrastructure.database.repositories.categories import CategoryRepository
from application.core.exceptions.domain_exceptions import ForbiddenActionException

logger = logging.getLogger(__name__)


class DeleteCategoryUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, category_id: int, is_superuser: bool = False) -> bool:
        if not is_superuser:
            error = ForbiddenActionException()
            logger.error(f'Attempting to delete a category {category_id} without superuser rights')
            raise error
        async with self._database.session() as session:
            await self._repo.delete(session=session, id=category_id)

        return True
