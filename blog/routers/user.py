
from typing import List
from fastapi import APIRouter, Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from .. import schemas ,database,models
from ..hashing import Hash
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=['Users']
    
)
get_db=database.get_db
# --- create user--
# pwd_cxt= CryptContext(schemes=['bcrypt'],deprecated='auto')
@router.post('/', response_model= schemas.showUser)
def create_user(request: schemas.User,db:Session = Depends(get_db)):
    # hashedPassword =pwd_cxt.hash(request.password)
    # new_user =models.User(name=request.name,email=request.email,password=hashedPassword)
    # print("Password length:", len(request.password))
    # print(hashing.Hash.bcrypt(request.password))
    # new_user =models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return request
    return user.create(request,db)

# ---end---

@router.get('/{id}',response_model=schemas.showUser)
def get_user(id:int,db:Session = Depends(get_db) ):
    # user= db.query(models.User).filter(models.User.id == id ).first()
    # if not user:
    #     raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail= f'Blog with the id {id} is not available')
    
    # return user
    return user.get(id,db)