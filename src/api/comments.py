from fastapi import APIRouter, status, HTTPException
from datetime import datetime
from src.schemas.comments import CommentCreateSchema, CommentResponseSchema, CommentUpdateSchema

router = APIRouter()

comments = []

@router.get('/get/{comment_id}',)
def get_comment(comment_id: int):
    if comment_id < len(comments):
        return comments[comment_id]
    else:
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND,)

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=CommentResponseSchema,)
def create_comment(comment: CommentCreateSchema) -> dict:
    response = {
        'id': len(comments),
        'post': comment.post,
        'author': comment.author,
        'text': comment.text,
        'created_at': datetime.now(),
    }
    comments.append(response)
    return CommentResponseSchema.model_validate(obj=response)

@router.put('/update/{comment_id}', status_code=status.HTTP_200_OK, response_model=CommentResponseSchema,)
def update_comment(comment_id: int, comment: CommentUpdateSchema) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND,)
    response = comments[comment_id]
    response['text'] = comment.text
    return CommentResponseSchema.model_validate(obj=response)

@router.delete('/delete/{comment_id}', status_code=status.HTTP_200_OK)
def delete_comment(comment_id: int) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(
            detail="Comment not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    comments.pop(comment_id)
    return {'message': "Comment has been deleted"}
