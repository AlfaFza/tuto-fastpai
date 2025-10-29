from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
@app.get('/')
def index():
    return {'data': 'Blog list'}

@app.get('/blog')
def inde(limit=10,published: bool= True,sort:Optional [str] =None):
    # only get 10 published blog
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:  
        return {'data':f'{limit} blogs from the db'}

 
@app.get('/blog/unpublished')
def unpublished():
    #fetch blog with id =id
    return {'data':'all unpublished Blogs'}

@app.get('/blog/{id}')
def show(id):
    #fetch blog with id =id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    #fetch comments blog with id =id
    return {'data':{'1','2'}}


#request body

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':"Blog is created {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)
# run python3 main.py 