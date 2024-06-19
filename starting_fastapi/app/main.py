from typing import Optional
from fastapi import FastAPI, Response , status , HTTPException
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

@app.post("/createposts" , status_code=status.HTTP_201_CREATED)                     
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

@app.get("/posts/{id}" ) # when ever we get a value from path it becomes string
def get_a_single_post(id : int , response : Response) :
    specific_post_id = find_posts_id(id) # So we will turn it into integer  ..... but instead of making it integer here we will assign a type to id so client will never put a value which not a number like id = asdasa
    if not specific_post_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return{"message" : f"post with id: {id} not found"}
    print(specific_post_id)
    return{
        #"details" : f"Here is posts_id >>>> {id} <<<< you are interested in "
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
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    my_db_my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# To update a method with PUT
@app.put("/posts/{id}")
def update_post_put(id:int , post : Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_db_my_posts[index] = post_dict
    return {"data" : post_dict}