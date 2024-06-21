from typing import Optional
from fastapi import FastAPI, Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content : str
    published : bool = True # True is set as default
    rating : Optional[int] = None

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


@app.get("/posts")
def get_posts_by_get_param():
    cursor.execute("""SELECT * FROM posts""")
    post = cursor.fetchall()
    return{
        "data" : post
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
def create_posts(new_post : Post):
    print(new_post)
    cursor.execute("""INSERT INTO posts (title , content , published) VALUES (%s , %s , %s) RETURNING * """ , (new_post.title , new_post.content , new_post.published))
    a_post = cursor.fetchone()
    conn.commit()
    return{
        "data" : a_post
    }
    

# Get a single post with id

@app.get("/posts/{id}" ) 
def get_a_single_post(id : int , response : Response) :
    cursor.execute("""SELECT * FROM posts WHERE id = %s""" , (str(id),))
    specific_post_id = cursor.fetchone()
    if not specific_post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    print(specific_post_id)
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
def delete(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """ , (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# To update a method with PUT
@app.put("/posts/{id}")
def update_post_put(id:int , post : Post):
    cursor.execute("""UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s RETURNING *""" , (post.title , post.content , post.published , (str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    return {"data" : updated_post}