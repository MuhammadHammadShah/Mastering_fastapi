from datetime import datetime
from pydantic import BaseModel



class PostBase(BaseModel):
    title: str
    content : str
    published : bool = True # True is set as default

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at : datetime
    # title: str
    # content : str       ## these are inherated from PostBase.
    # published : bool   

    class Config:
        orm_mode = True 