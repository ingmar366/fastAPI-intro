from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    # creates a blueprint of the columns in the database and what data is exceptedc for these columns
    __tablename__= 'blogs'
    id=Column(Integer,primary_key=True, index=True)
    title= Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship( "User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id=Column(Integer,primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)

    blogs = relationship( "Blog", back_populates="creator")


