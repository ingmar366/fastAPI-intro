from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schemas, database, models, oaut2
from typing import  List
from sqlalchemy.orm import  Session
from ..repository import blog



router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

# status code changes the return value after succesfull creating a new item
@router.post('/', status_code=status.HTTP_201_CREATED)

#request controls the input data that can be put in
def create(request: schemas.Blog, db : Session = Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
   return blog.create(request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id})',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog,db:Session = Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.update(id, request, db)

# return value is multiple values, therefor it is needed to put into a list
@router.get('/',response_model = List[schemas.ShowBlog])
def all(db : Session = Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_all(db)
    

# response model controls the data that will be given back from the call.
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db : Session = Depends(database.get_db),current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.show(id,db)

