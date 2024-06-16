from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content : str
    published : bool = True # True is set as default
    rating : Optional[int] = None



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


@app.get("/")
async def root():
    return {
        "message": "Hello to this  World"
    }


@app.get("/posts")
def get_posts_get_param():
    return {
        "data": my_db_my_posts
        }
        #"message_for_you": "This is your posts" >>>> this one was before but now we will get data from db
    
    
@app.post("/first_create_posts")
def first_creates_post(payload:dict = Body(...)): #Body is an object from fastapi.params and which geets data from body as we saw in postman 
    print(payload)                          #body area and according to this function it also assigned the value to payload which we will
                                            # print inside the function
    return{
"new_message" : f"title: {payload['title']} content: {payload['content']} description: {payload['description']}" #{payload['title]} y blkl aese hi h jese hm sir nasir ki class m f-string wala prthy thy aur f-string k dynamically kch dene k liye {} use krty thy 
# aur ab yahan payload m b 2 values a rahi hn jn ko recieve krne ka tareeka ye h pehle f-string m payload ko liye phir payload kki values le li. {payload[title]} or {payload[content]}
    }          

@app.post("/createposts")                     
def create_posts(new_post : Post): # we can make this post request to get requests by send the param new_post in return 
    print(new_post)# to add some data our db my_db_my_posts but we have to give random numbers to id's for our db so we will also use randomrange packages
    new_post_dict = new_post.dict()
    new_post_dict["id"] = randrange(0,1000000000000)
    my_db_my_posts.append(new_post_dict)

    #print(new_post.dict()) # .dict() can make values into dictionary again.
    return{
        "data" : new_post
    }
    

# Get a single post with id

@app.get("/posts/{id}") # when ever we get a value from path it becomes string
def get_a_single_post(id):
    specific_post_id = find_posts_id(int(id)) # So we will turn it into integer 
    #print(id)
    print(specific_post_id)
    return{
        #"details" : f"Here is posts_id >>>> {id} <<<< you are interested in "
          "details" :  specific_post_id
    }
