from typing import List, Optional
from fastapi import FastAPI, Response , status , HTTPException , Depends
from fastapi.params import Body
from passlib.context import CryptContext
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import  models , schemas
from .database import  engine , get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost' , database='fastapi_db' , user='postgres' , password='POSTGRESforPIAIC.6/11/2024' , cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was Successfull! ")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: " , error)
        time.sleep(4)


my_db_my_posts = [{
    "title" : "title of post 1",
    "content" : "content of post 1",
    "id" : 1
},
{
    "title" : "favourite foods",
    "content" : "I like pizza",
    "id" : 2
}] # this is a self made database for simple use

#function to match the id's in our own db my_db_my_posts
def find_posts_id(id):
    for p in my_db_my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id): # enumerate get index and id both so here it will assign index to i and id to p 
    for i , p in enumerate(my_db_my_posts):
        if p["id"] == id:
            return i



@app.get("/")
async def root():
    return {
        "message": "Hello to this  World " 
    }


@app.get("/posts" , response_model=List[schemas.Post])
def get_posts_by_get_param(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
    
              

@app.post("/createposts" , status_code=status.HTTP_201_CREATED , response_model=schemas.Post)                     
def create_posts(new_post : schemas.PostCreate , db: Session = Depends(get_db)):
    #a_post = models.Post(title = new_post.title , content = new_post.content , published = new_post.published ) # This way was ineffecient because if we get a fifty fields in our model so we have to write fifty fields here so we will use the unpacking dicttionary method here
    a_post = models.Post(**new_post.dict()) # Here we are using the unpacking dictionary , >>> It wil automatically unpack all the field whatever no problem how many are they in models.
    db.add(a_post)
    db.commit()
    db.refresh(a_post)

    return a_post
    


# Get a single post with id

@app.get("/posts/{id}" , response_model=schemas.Post ) 
def get_a_single_post(id : int , response : Response , db: Session = Depends(get_db)) :
#    cursor.execute("""SELECT * FROM posts WHERE id = %s""" , (str(id),))
#    specific_post_id = cursor.fetchone()
    specific_post_id = db.query(models.Post).filter(models.Post.id == id).first()
    #print(specific_post_id)
    if not specific_post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #print(specific_post_id)
    return specific_post_id
    


# To delete a post

@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int , db: Session = Depends(get_db)):
    
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# To update a method with PUT

@app.put("/posts/{id}" , status_code=status.HTTP_202_ACCEPTED , response_model=schemas.Post)
def update_post_put(id:int , post : schemas.PostCreate , db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #post_query.update({'title' : "updated from vs code" , 'content' : "content of updated from vs code"} , synchronize_session=False)
    post_query.update(post.dict() , synchronize_session=False)
    db.commit()
    return post_query.first()


# Now creating method for table "users"

@app.post("/create_users" , status_code=status.HTTP_201_CREATED , response_model=schemas.UserOut)    
def create_user(user : schemas.UserCreate , db: Session = Depends(get_db)):
    # hash the password which is retrieving from user.password 
    hashed_password = pwd_context.hash(user.password)  # It hashes the user password before assigning
    user.password = hashed_password # It assigned the user's hashed_password which was hashed in above line
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user