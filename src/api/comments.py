from datetime import datetime

from fastapi import APIRouter, status, HTTPException

from src.schemas.comments import CommentResponseSchema, CommentUpdateSchema, CommentCreateSchema

router = APIRouter()

comments = []

@router.get('/comments/{comment_id}')
async def get_comment(comment_id: int):
    if comment_id < len(comments):
        return comments[comment_id]
    else:
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND)

@router.get('/comments')
async def get_all_comments(post_id: int):
    post_comments = [comment for comment in comments if comment.get("post") == post_id]
    if not post_comments:
        raise HTTPException(
            detail="No comments found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return post_comments

@router.post('/comments', status_code=status.HTTP_201_CREATED, response_model=CommentResponseSchema)
async def create_comment(comment: CommentCreateSchema) -> dict:
    response = {
        'id': len(comments),
        'post': comment.post,
        'author': comment.author,
        'text': comment.text,
        'created_at': datetime.now(),
    }
    comments.append(response)
    return CommentResponseSchema.model_validate(obj=response)

@router.put('/comments/{comment_id}', status_code=status.HTTP_200_OK, response_model=CommentResponseSchema)
async def update_comment(comment_id: int, comment: CommentUpdateSchema) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(detail="Comment not found", status_code=status.HTTP_404_NOT_FOUND,)
    response = comments[comment_id]
    response['text'] = comment.text
    return CommentResponseSchema.model_validate(obj=response)

@router.delete('/comments/{comment_id}', status_code=status.HTTP_200_OK)
async def delete_comment(comment_id: int) -> dict:
    if comment_id >= len(comments):
        raise HTTPException(
            detail="Comment not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    comments.pop(comment_id)
    return {'message': "Comment has been deleted"}
