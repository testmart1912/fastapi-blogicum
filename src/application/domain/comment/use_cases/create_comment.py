from datetime import datetime, timezone

from application.infrastructure.database.database import database
from application.infrastructure.database.repositories.comments import CommentRepository
from application.schemas.comments import CommentResponseSchema, CommentCreateSchema


class CreateCommentUseCase:
    def __init__(self):
        self._database = database
        self._repo = CommentRepository()

    async def execute(self, dto: CommentCreateSchema, author_id: int) -> CommentResponseSchema:
        async with self._database.session() as session:
            comment = await self._repo.create(
                session=session,
                text=dto.text,
                author_id=author_id,
                post_id=dto.post_id,
                created_at=datetime.now(timezone.utc).replace(tzinfo=None),
            )
            await session.flush()
            comment_with_relations = await self._repo.get_by_id_with_relations(
                session=session, comment_id=comment.id
            )

        return CommentResponseSchema.model_validate(obj=comment_with_relations)
