from typing import Optional
from fastapi import FastAPI, Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import  models
from .database import  engine , get_db



models.Base.metadata.create_all(bind=engine)

app = FastAPI()




class Post(BaseModel):
    title: str
    content : str
    published : bool = True # True is set as default


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
        "message": "Hello to this  World"
    }


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()

    return {
        "data" : posts
    }



@app.get("/posts")
def get_posts_by_get_param(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return{
        "data" : posts
    }
    
    
@app.post("/first_create_posts")
def first_creates_post(payload:dict = Body(...)): #Body is an object from fastapi.params and which geets data from body as we saw in postman 
    print(payload)                          #body area and according to this function it also assigned the value to payload which we will
                                            # print inside the function
    return{
"new_message" : f"title: {payload['title']} content: {payload['content']} description: {payload['description']}" #{payload['title]} y blkl aese hi h jese hm sir nasir ki class m f-string wala prthy thy aur f-string k dynamically kch dene k liye {} use krty thy 
# aur ab yahan payload m b 2 values a rahi hn jn ko recieve krne ka tareeka ye h pehle f-string m payload ko liye phir payload kki values le li. {payload[title]} or {payload[content]}
    }          

@app.post("/createposts" , status_code=status.HTTP_201_CREATED)                     
def create_posts(new_post : Post , db: Session = Depends(get_db)):
    #a_post = models.Post(title = new_post.title , content = new_post.content , published = new_post.published ) # This way was ineffecient because if we get a fifty fields in our model so we have to write fifty fields here so we will use the unpacking dicttionary method here
    a_post = models.Post(**new_post.dict()) # Here we are using the unpacking dictionary , >>> It wil automatically unpack all the field whatever no problem how many are they in models.
    db.add(a_post)
    db.commit()
    db.refresh(a_post)

    return{
        "data" : a_post
    }



# Get a single post with id

@app.get("/posts/{id}" ) 
def get_a_single_post(id : int , response : Response , db: Session = Depends(get_db)) :
#    cursor.execute("""SELECT * FROM posts WHERE id = %s""" , (str(id),))
#    specific_post_id = cursor.fetchone()
    specific_post_id = db.query(models.Post).filter(models.Post.id == id).first()
    #print(specific_post_id)
    if not specific_post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #print(specific_post_id)
    return{
          "details" :  specific_post_id
    }

# TO get latest post but in this we get error

#@app.get("/posts/latest")
#def get_latest_post():
#    post = my_db_my_posts[len(my_db_my_posts)-1]
#    return {"detail" : post}


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
@app.put("/posts/{id}")
def update_post_put(id:int , post : Post , db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    #post_query.update({'title' : "updated from vs code" , 'content' : "content of updated from vs code"} , synchronize_session=False)
    post_query.update(post.dict() , synchronize_session=False)
    db.commit()
    return {"data" : post_query.first()}
