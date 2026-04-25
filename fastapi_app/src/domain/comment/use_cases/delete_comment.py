import logging

from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.comments import CommentRepository
from src.core.exceptions.domain_exceptions import ForbiddenActionException

logger = logging.getLogger(__name__)


class DeleteCommentUseCase:
    def __init__(self):
        self._database = database
        self._repo = CommentRepository()

    async def execute(
            self,
            comment_id: int,
            user_id: int,
            is_staff: bool = False,
            is_superuser: bool = False) -> bool:
        with self._database.session() as session:
            comment = self._repo.get_by_id(session=session, id=comment_id)

            if not (is_superuser or is_staff or comment.author_id == user_id):
                error = ForbiddenActionException()
                logger.error(
                    f'User {user_id} attempted to delete someone else\'s comment {comment_id} '
                    f'(author: {comment.author_id})'
                )
            self._repo.delete(session=session, id=comment_id)

        return True
