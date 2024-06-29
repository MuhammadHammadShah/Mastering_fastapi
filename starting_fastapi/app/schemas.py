from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr  , field_validator
from pydantic.types import conint



class PostBase(BaseModel): # Request
    title: str
    content : str
    published : bool = True # True is set as default

class PostCreate(PostBase):
    pass


class UserOut(BaseModel): # Response
    id : int              # In response we get sqlalchemy model so we need to convert it into regular pydantic model.
    email: EmailStr
    created_at : datetime

    class Config:         # this will convert the sqlalchemy model to regular pydantic model.
        from_attributes = True


class Post(PostBase): # Response
    id: int
    created_at : datetime
    owner_id : int
    # title: str
    # content : str       ## these are inherated from PostBase.
    # published : bool   
    owner : UserOut


    class Config:
    #    orm_mode = True  # a warning was coming in terminal so i changed it >>> the warning
                         # >>>>> site-packages\pydantic\_internal\_config.py:334: UserWarning: Valid config keys have changed in V2:* 'orm_mode' has been renamed to 'from_attributes'warnings.warn(message, UserWarning)
        from_attributes = True

# Class for votes
class PostOut(PostBase): # response   
    post : Post
    votes : int
    class Config:
        from_attributes = True

# Class for Users:

class UserCreate(BaseModel): # Request
    email : EmailStr
    password : str




class UserLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    #id : Optional[str] = None
    id : int


class Vote(BaseModel):
    post_id : int
    dir: int

    @field_validator('dir')
    @classmethod
    def validate_dir(cls, v):
        if v not in [0, 1]:
            raise ValueError("Vote direction must be either 1 (upvote) or 0 (down vote)")
        return v



