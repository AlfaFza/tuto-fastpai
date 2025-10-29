from typing import List
from fastapi import APIRouter, Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from .. import schemas ,database,models
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


get_db=database.get_db

@router.get('/',response_model=List[schemas.showBlog],)
def all(db:Session = Depends(database.get_db)):
    # blogs= db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request:schemas.Blog,db:Session = Depends(database.get_db)):
    # new_blog = models.Blog(title=blog.title, body=blog.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request,db)


# delete a blog
@router.post('/{id}',status_code=status.HTTP_204_NO_CONTENT, )
def destroy(id:int,db:Session = Depends(get_db)):
    # blog= db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail= f'Blog with the id {id} is not available')
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.destroy(id,db)

# ---end---


# update blog

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED ,)
def update(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail= f'Blog with the id {id} is not available')
    # blog.update(request.dict())
    # db.commit()
    # return "updated"
    return blog.update(id,request,db)
    
# --end--

# getting particular blog with id 

@router.get('/{id}', status_code=200,response_model=schemas.showBlog,)
def show(id:int ,db:Session = Depends(get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail= f'Blog with the id {id} is not available')
      
    # return blog
    return blog.show(id,db)


# --end---