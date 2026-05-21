import logging

from application.infrastructure.database.database import database
from application.infrastructure.database.repositories.posts import PostRepository
from application.infrastructure.database.repositories.categories import CategoryRepository
from application.infrastructure.database.repositories.locations import LocationRepository
from application.schemas.posts import PostResponseSchema, PostUpdateSchema
from application.core.exceptions.domain_exceptions import CategoryNotFoundByIdException
from application.core.exceptions.domain_exceptions import LocationNotFoundByIdException
from application.core.exceptions.domain_exceptions import ForbiddenActionException

logger = logging.getLogger(__name__)


class UpdatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()
        self._category_repo = CategoryRepository()
        self._location_repo = LocationRepository()

    async def execute(
        self,
        post_id: int,
        dto: PostUpdateSchema,
        user_id: int,
        is_staff: bool = False,
        is_superuser: bool = False) -> PostResponseSchema:
        async with self._database.session() as session:
            post = await self._repo.get_by_id(session=session, id=post_id)

            if not (is_superuser or is_staff or post.author_id == user_id):
                error = ForbiddenActionException()
                logger.error(
                    f'User {user_id} attempted to update someone else\'s post {post_id} '
                    f'(author: {post.author_id})'
                )
                raise error
            if dto.category_id is not None:
                try:
                    await self._category_repo.get_by_id(session, dto.category_id)
                except CategoryNotFoundByIdException as e:
                    logger.error(f'Category {dto.category_id} not found')
                    raise e

            if dto.location_id is not None:
                try:
                    await self._location_repo.get_by_id(session, dto.location_id)
                except LocationNotFoundByIdException as e:
                    logger.error(f'Location {dto.location_id} not found')
                    raise e

            post = await self._repo.update(
                session=session,
                id=post_id,
                title=dto.title,
                text=dto.text,
                is_published=dto.is_published,
                category_id=dto.category_id,
                location_id=dto.location_id,
                image_path=dto.image_path
            )
            await session.commit()
            await session.refresh(post)
            post_with_relations = await self._repo.get_by_id_with_relations(
                session=session, post_id=post.id
            )

        return PostResponseSchema.model_validate(obj=post_with_relations)
