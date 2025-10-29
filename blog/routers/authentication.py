from fastapi import APIRouter,Depends,HTTPException,status

from ..hashing import Hash
from .. import schemas ,database,models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone

from jose import JWTError,jwt
from ..token import create_access_token

router= APIRouter(
    prefix="/login",
    tags=['Authentication']
)

@router.post('/')
def login(request: schemas.Login,db:Session = Depends(database.get_db)):
    user=db.query(models.user).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'Invalid Credentials')
        
        # verify the password 
        
    if Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'Incorrect Password')
        
    # generate JWT token and return it
    access_token = create_access_token(data={"sub": user.email})
    
    return (access_token=access_token, token_type="bearer")