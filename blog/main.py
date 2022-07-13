from fastapi import FastAPI

from blog.routers import authentication
from . import models
from .database import engine
from .routers import blog, user


#setting up de base app
app = FastAPI()

#when find a model create a database for it.
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)









