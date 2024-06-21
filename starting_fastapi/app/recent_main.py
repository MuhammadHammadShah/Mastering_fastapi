

## previous method to fetch data through GET method


#@app.get("/posts")
#def get_posts_by_get_param():
  #  return {
 #       "data": my_db_my_posts
#        }
#"message_for_you": "This is your posts" >>>> this one was before but now we will get data from db


## previous method to create a post through POST method

#@app.post("/createposts" , status_code=status.HTTP_201_CREATED)                     
#def create_posts(new_post : Post): # we can make this post request to get requests by send the param new_post in return 
#    print(new_post)# to add some data our db my_db_my_posts but we have to give random numbers to id's for our db so we will also use randomrange packages
#    new_post_dict = new_post.dict()
#    new_post_dict["id"] = randrange(0,1000000000000)
#    my_db_my_posts.append(new_post_dict)
#
#    #print(new_post.dict()) # .dict() can make values into dictionary again.
#    return{
#        "data" : new_post
#    }


## Get a single post with id
#@app.get("/posts/{id}" ) # when ever we get a value from path it becomes string
#def get_a_single_post(id : int , response : Response) :
#    specific_post_id = find_posts_id(id) # So we will turn it into integer  ..... but instead of making it integer here we will assign a type to id so client will never put a value which not a number like id = asdasa
#    if not specific_post_id:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
#        #response.status_code = status.HTTP_404_NOT_FOUND
#        #return{"message" : f"post with id: {id} not found"}
#    print(specific_post_id)
#    return{
#        #"details" : f"Here is posts_id >>>> {id} <<<< you are interested in "
#          "details" :  specific_post_id
#    }


## To delete a post
#@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
#def delete(id : int):
#    index = find_index_post(id)
#    if index == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
#    my_db_my_posts.pop(index)
#    return Response(status_code=status.HTTP_204_NO_CONTENT)


## To update a method with PUT
#@app.put("/posts/{id}")
#def update_post_put(id:int , post : Post):
#    index = find_index_post(id)
#    if index == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} not found")
#    post_dict = post.dict()
#    post_dict['id'] = id
#    my_db_my_posts[index] = post_dict
#    return {"data" : post_dict}