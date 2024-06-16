from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello to this  World"
    }
@app.get("/posts")
def root():
    return {
        "message": "This is your posts"
    }
    
@app.post("/createposts")
def create_posts(payload:dict = Body(...)): #Body is an object from fastapi.params and which geets data from body as we saw in postman 
    print(payload)                          #body area and according to this function it also assigned the value to payload which we will
                                            # print inside the function
    return{
"new_message" : f"title: {payload['title']} content: {payload['content']} description: {payload['description']}" #{payload['title]} y blkl aese hi h jese hm sir nasir ki class m f-string wala prthy thy aur f-string k dynamically kch dene k liye {} use krty thy 
# aur ab yahan payload m b 2 values a rahi hn jn ko recieve krne ka tareeka ye h pehle f-string m payload ko liye phir payload kki values le li. {payload[title]} or {payload[content]}
    }                               
    
