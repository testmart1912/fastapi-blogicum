from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.comments import CommentRepository
from src.schemas.comments import CommentResponseSchema


class GetCommentByIdUseCase:
    def __init__(self):
        self._database = database
        self._repo = CommentRepository()

    async def execute(self, comment_id: int) -> CommentResponseSchema:
        with self._database.session() as session:
            comment = self._repo.get_by_id_with_relations(session=session, comment_id=comment_id)

        return CommentResponseSchema.model_validate(obj=comment)
