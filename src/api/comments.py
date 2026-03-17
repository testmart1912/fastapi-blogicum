from datetime import datetime

from fastapi import APIRouter, status, HTTPException

from src.schemas.comments import CommentSchema, CommentSchema, CommentUpdateSchema

router = APIRouter()

comments = []

@router.get('/get/{comment_id}')
def get_comment(comment_id: int):
    if comment_id < len(comments):
        return comments[comment_id]
    else:
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND)

@router.get('/get-all')
def get_all_comments():
    if not comments:
        raise HTTPException(
            detail="No comments found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return comments

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=CommentSchema)
def create_comment(comment: CommentSchema) -> dict:
    response = {
        'id': len(comments),
        'post': comment.post,
        'author': comment.author,
        'text': comment.text,
        'created_at': datetime.now(),
    }
    comments.append(response)
    return CommentSchema.model_validate(obj=response)

@router.put('/update/{comment_id}', status_code=status.HTTP_200_OK, response_model=CommentSchema)
def update_comment(comment_id: int, comment: CommentUpdateSchema) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND,)
    response = comments[comment_id]
    response['text'] = comment.text
    return CommentSchema.model_validate(obj=response)

@router.delete('/delete/{comment_id}', status_code=status.HTTP_200_OK)
def delete_comment(comment_id: int) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(
            detail="Comment not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    comments.pop(comment_id)
    return {'message': "Comment has been deleted"}
