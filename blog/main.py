from fastapi import FastAPI
from .database import engine
from . import schemas, models
from .routers import blog ,user,authentication



app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)







# for posting to db 
# def get_db():
#     db = Sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED,tags=['blog'] )
# def create(blog:schemas.Blog,db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=blog.title, body=blog.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
# ---end---

# # delete a blog
# @app.post('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
# def destroy(id,db:Session = Depends(get_db)):
#     blog= db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail= f'Blog with the id {id} is not available')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# # ---end---

# # update blog

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED ,tags=['blog'])
# def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail= f'Blog with the id {id} is not available')
#     blog.update(request.dict())
#     db.commit()
#     return "updated"
    


# # --end--
# get from db 
# @app.get('/blog',response_model=List[schemas.showBlog],tags=['blog'])
# def all(db:Session = Depends(get_db)):
#     blogs= db.query(models.Blog).all()
#     return blogs

# # getting particular blog with id 

# @app.get('/blog/{id}', status_code=200,response_model=schemas.showBlog,tags=['blog'])
# def show(id,response: Response ,db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail= f'Blog with the id {id} is not available')
#         # response.status_code= status.HTTP_404_NOT_FOUND
#         # return {'details': f'Blog with the id {id} is not available'}
#     return blog


# # --end---

# # --- create user--
# # pwd_cxt= CryptContext(schemes=['bcrypt'],deprecated='auto')
# @app.post('/user', response_model= schemas.showUser,tags=['User'])
# def create_user(request: schemas.User,db:Session = Depends(get_db)):
#     # hashedPassword =pwd_cxt.hash(request.password)
#     # new_user =models.User(name=request.name,email=request.email,password=hashedPassword)
#     print("Password length:", len(request.password))
#     print(hashing.Hash.bcrypt(request.password))
#     # new_user =models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    
#     # db.add(new_user)
#     # db.commit()
#     # db.refresh(new_user)
#     return request

# # ---end---

# @app.get('/user/{id}',response_model=schemas.showUser,tags=['User'])
# def get_user(id:int,db:Session = Depends(get_db) ):
#     user= db.query(models.User).filter(models.User.id == id ).first()
#     if not user:
#         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail= f'Blog with the id {id} is not available')
    
#     return user