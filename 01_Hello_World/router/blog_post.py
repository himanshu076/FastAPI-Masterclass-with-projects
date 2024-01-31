from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

class Image(BaseModel):
  url: str
  alias: str

class BlogModel(BaseModel):
  title: str
  content: str
  number_of_comments: int
  published: bool
  tags: list[str] = [],
  metadata: dict[str, str] = {'key': 'value'}
  image: Image | None = None

  # def __init__(self, **data):
  #   super().__init__(**data)
  #   self.tags = self.tags if self.tags is not None else []
  #   self.metadata = self.metadata if self.metadata is not None else {'key': 'value'}

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
  return {'id': id,
          'data': blog,
          'version': version
          }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_title: int = Query(None,
                    title='title of the comment',
                    description='Some description for comment_title',
                    alias='commentTitle',
                    deprecated=True
                    ),
                    # content: str = Body('hi how are you')
                    content: str = Body(...,
                      min_length=10,
                      max_length=50,
                      regex='^[a-z\s]*$'),
                    v: list[str] | None = Query(['1.0', '1.1', '1.2']),
                    comment_id: int = Path(gt=5, le=10)
                  ):
  return {
    'blog': blog,
    'id': id,
    'comment_title': comment_title,
    'content': content,
    'version': v,
    'comment_id': comment_id
  }

def required_functionality():
  return {'message': 'Learning FastApi is important'}
