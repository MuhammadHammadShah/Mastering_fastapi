from fastapi import FastAPI
# from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
# from .config import settings

# print(settings.database_username)

# models.Base.metadata.create_all(bind=engine) # commented it because everything is now done with alembic

app = FastAPI()
# origin = ["https://www.google.com"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {
        "message": "Hello to this  World "
    }
