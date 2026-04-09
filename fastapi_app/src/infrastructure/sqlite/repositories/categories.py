from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.infrastructure.sqlite.repositories.base import BaseRepository
from src.infrastructure.sqlite.models.categories import Category
from src.core.exceptions.domain_exceptions import CategoryNotFoundByIdException
from src.core.exceptions.domain_exceptions import CategoryNotFoundBySlugException
from src.core.exceptions.database_exceptions import CategorySlugConflictException


class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category, CategoryNotFoundByIdException)

    def get_by_slug(self, session: Session, slug: str) -> Category:
        query = session.query(self._model).where(self._model.slug == slug)
        category = query.scalar()
        if not category:
            raise CategoryNotFoundBySlugException(slug)
        return category

    def create(self, session: Session, **kwargs) -> Category:
        try:
            return super().create(session=session, **kwargs)
        except IntegrityError:
            raise CategorySlugConflictException()
