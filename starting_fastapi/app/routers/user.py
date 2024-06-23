from fastapi import APIRouter, status , HTTPException , Depends
from sqlalchemy.orm import Session
from .. import  models , schemas , utils
from ..database import  get_db

# Creating a router instead of @app

router = APIRouter()

# To Create user for "user's table"

@router.post("/create_users" , status_code=status.HTTP_201_CREATED , response_model=schemas.UserOut)    
def create_user(user : schemas.UserCreate , db: Session = Depends(get_db)):
    # hash the password which is retrieving from user.password 
    hashed_password = utils.hash(user.password)  # It hashes the user password before assigning
    user.password = hashed_password # It assigned the user's hashed_password which was hashed in above line
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# To get a specific user 

@router.get("/users/{id}" , response_model=schemas.UserOut)
def get_user(id : int , db : Session = Depends(get_db)):
    a_user = db.query(models.User).filter(models.User.id == id).first()
    if not a_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return a_user
