from fastapi import APIRouter, Response, status
from enum import Enum

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

# @router.get('/blog/all')
# def get_all_blog():
#   return {'message': 'All blogs provided'}

@router.get('/all',
         summary='Retrive all blogs',
         description='This api call simulates featching all blogs.',
         response_description='The list of available blogs')
def get_all_blog(page, page_size: str | None = None):
  return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: str | None = None):
  """
  Simulates retrieving a comment of a blog

  - **id** mandatory path parameter
  - **comment_id** mandatory path parameter
  - **valid** optional query parameter
  - **Username** optional query parameter
  """
  return {'message': f'blog_id {id} comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'Blog type is {type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} not found'}

  response.status_code = status.HTTP_200_OK
  return {'message': f'Blog with id {id}'}
