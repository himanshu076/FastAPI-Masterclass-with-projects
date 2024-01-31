from pydantic import BaseModel


# *********** Note - Schema is used to validate the type of the request parameter is valid or not and display the database structure.

# Article inside UserDisplay
class Article(BaseModel):
  title: str
  content: str
  published: bool

  class Config():
    # orm_mode has been renamed as - from_attributes.
    from_attributes=True

class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  items: list[Article] = []

  class Config():
    # orm_mode has been renamed as - from_attributes.
    from_attributes=True

# User inside ArticleDisplay
class User(BaseModel):
  id: int
  username: str

  class Config():
    # orm_mode has been renamed as - from_attributes.
    from_attributes=True

class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User

  class Config():
    # orm_mode has been renamed as - from_attributes.
    from_attributes=True