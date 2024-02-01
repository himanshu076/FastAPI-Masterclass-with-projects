from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

from router import blog_get, blog_post, user, article, product
from db import models
from db.database import engine
from exceptions import StoryException


app = FastAPI()

origins = [
  'http://127.0.0.1:3000'
]

app.add_middleware(
  CORSMiddleware(allow_origins=origins, allow_credentials=True,
                 allow_methods=['*'], allow_headers=['*'])
)

app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
  return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT, content={'detail': exc.name})

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#   return PlainTextResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': exc.name})

models.Base.metadata.create_all(engine)
