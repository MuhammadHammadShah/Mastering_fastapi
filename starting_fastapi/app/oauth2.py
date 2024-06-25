import jwt
from jwt.exceptions import InvalidTokenError , PyJWTError
from datetime import datetime , timedelta
from . import schemas
from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
# Algorithm
# Expiration time

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Funct to create an access token

def create_access_token(data : dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM) # here i think to_encode is a payload
    return encoded_jwt


# Funct to verify the access token

def verify_access_token(token : str , credentials_exception):

    try:
        paylaod = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
        id : str = paylaod.get("user_id")    # To extract the data 
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
        # token_data = schemas.TokenData(id=str(id))

    except PyJWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token : str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                                          detail="Could not Validate Credentials" , headers={"WWW-Authenticate" : "Bearer"})
    return verify_access_token(token , credentials_exception)