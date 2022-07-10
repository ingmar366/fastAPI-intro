from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True, sort: Optional[str]= None):
    #only get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs of the db'}
    return {'data':'all blogs returned'}
    
@app.get('/blog/unplublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id = id
    return{'data':id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return limit
    return {'data':{'1','2'}}



    #  posting

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'Blog is created with title {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)