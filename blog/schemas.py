from typing import List, Optional
from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        orm_mode =True

        
class User(BaseModel):
    name:str
    email:str
    password:str= Field(..., max_length=72)
    
class showUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] = []
    class Config:
        orm_mode =True
        
        
class showBlog(BaseModel):
    title: str
    body: str
    creator:Optional[showUser] = None
    class Config:
        orm_mode =True
        
        
class Login(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None