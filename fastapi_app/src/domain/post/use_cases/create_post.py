from datetime import datetime

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.posts import PostRepository
from src.schemas.posts import PostResponseSchema, PostCreateSchema
from src.infrastructure.sqlite.repositories.categories import CategoryRepository
from src.infrastructure.sqlite.repositories.locations import LocationRepository


class CreatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()
        self._category_repo = CategoryRepository()
        self._location_repo = LocationRepository()

    async def execute(self, dto: PostCreateSchema) -> PostResponseSchema:
        with self._database.session() as session:
            if dto.category_id is not None:
                self._category_repo.get_by_id(session, dto.category_id)
            if dto.location_id is not None:
                self._location_repo.get_by_id(session, dto.location_id)
            post = self._repo.create(
                session=session,
                title=dto.title,
                text=dto.text,
                is_published=dto.is_published,
                created_at=datetime.now(),
                pub_date=dto.pub_date,
                author_id=dto.author_id,
                category_id=dto.category_id,
                location_id=dto.location_id,
                image=dto.image or '',
            )
            session.flush()
            post_with_relations = self._repo.get_by_id_with_relations(
                session=session, post_id=post.id
            )

        if post_with_relations is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Created post could not be loaded',
            )

        missing_relations = []
        if post_with_relations.author is None:
            missing_relations.append(f"author_id={dto.author_id}")
        if post_with_relations.location is None:
            missing_relations.append(f"location_id={dto.location_id}")
        if post_with_relations.category is None:
            missing_relations.append(f"category_id={dto.category_id}")

        if missing_relations:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Related entities not found: {', '.join(missing_relations)}",
            )

        return PostResponseSchema.model_validate(obj=post_with_relations)
