from pydantic import BaseModel
from typing import List
from typing import Union


class BlogBase(BaseModel):
# creates a base scheme based on the Basemodel. it gives a representation of the data that has to be put into the db
    title:str
    body: str
    

class Blog(BlogBase):
    class Config():
        orm_mode = True




class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator: ShowUser
    # is needed because pydantic is being used as orm
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None