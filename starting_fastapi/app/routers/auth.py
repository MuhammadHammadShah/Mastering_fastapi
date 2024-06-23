from fastapi import APIRouter , Depends , HTTPException , Response , status
from sqlalchemy.orm import Session

from .. import database , schemas , models , utils

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def login(user_credentials: schemas.UserLogin ,db:Session=Depends(database.get_db)):
    # Implement login functionality
    user = db.query(models.User).filter(models.User.email == user_credentials.email ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Invalid Credentials")
    
    if not utils.verify_hashed_passwords(user_credentials.password , user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid Credentials")

    # create a token 
    # return token