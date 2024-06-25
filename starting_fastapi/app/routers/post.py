from typing import List
from fastapi import APIRouter, Response , status , HTTPException , Depends
from sqlalchemy.orm import Session
from .. import  models , schemas , oauth2
from ..database import  get_db

# Creating a router instead of @app

router = APIRouter(
    prefix="/posts",   
    tags=["Posts"]
)





@router.get("/" , response_model=List[schemas.Post])
def get_posts_by_get_param(db: Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts
    
              

@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schemas.Post)                     
def create_posts(new_post : schemas.PostCreate , db: Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user)):
    print(current_user)
    #a_post = models.Post(title = new_post.title , content = new_post.content , published = new_post.published ) # This way was ineffecient because if we get a fifty fields in our model so we have to write fifty fields here so we will use the unpacking dicttionary method here
    a_post = models.Post(**new_post.dict()) # Here we are using the unpacking dictionary , >>> It wil automatically unpack all the field whatever no problem how many are they in models.
    db.add(a_post)
    db.commit()
    db.refresh(a_post)

    return a_post
    


# Get a single post with id

@router.get("/{id}" , response_model=schemas.Post ) 
def get_a_single_post(id : int , response : Response , db: Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user)) :
#    cursor.execute("""SELECT * FROM posts WHERE id = %s""" , (str(id),))
#    specific_post_id = cursor.fetchone()
    specific_post_id = db.query(models.Post).filter(models.Post.id == id).first()
    #print(specific_post_id)
    if not specific_post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #print(specific_post_id)
    return specific_post_id
    


# To delete a post

@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int , db: Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user)):
    print(current_user)
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# To update a method with PUT

@router.put("/{id}" , status_code=status.HTTP_202_ACCEPTED , response_model=schemas.Post)
def update_post_put(id:int , post : schemas.PostCreate , db: Session = Depends(get_db) , current_user : int = Depends(oauth2.get_current_user)):
    print(current_user)
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #post_query.update({'title' : "updated from vs code" , 'content' : "content of updated from vs code"} , synchronize_session=False)
    post_query.update(post.dict() , synchronize_session=False)
    db.commit()
    return post_query.first()
