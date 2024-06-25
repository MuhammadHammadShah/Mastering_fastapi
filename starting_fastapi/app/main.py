from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import  models 
from .database import  engine 
from .routers import post , user , auth

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


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {
        "message": "Hello to this  World " 
    }
