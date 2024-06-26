from fastapi import APIRouter , Depends , HTTPException , Response , status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database , schemas , models , utils , oauth2

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login" , response_model=schemas.Token)
#def login(user_credentials: schemas.UserLogin ,db:Session=Depends(database.get_db)):
def login(user_credentials: OAuth2PasswordRequestForm = Depends() ,db:Session=Depends(database.get_db)):
    # Implement login functionality

## Now user_credential creates a form in which in creates a dict() by itself with a username and a password
# {
#     "username" : "blaaaaa",
#     "password" : "blaaaaa"
# }

    # user = db.query(models.User).filter(models.User.email == user_credentials.email ).first()
    user = db.query(models.User).filter(models.User.email == user_credentials.username ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid Credentials")
    
    if not utils.verify_hashed_passwords(user_credentials.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid Credentials")

    # create a token 
    # return token
    access_token = oauth2.create_access_token(data= {"user_id" : user.id}) # Here "user_id" is payload which i studiet at https://www.youtube.com/watch?v=0sOvCWFmrtA&t=24423s
    return{
        "access_token" : access_token , "token_type" : "bearer"
        }  # Here "bearer" is the type of token which is used in HTTP headers.
