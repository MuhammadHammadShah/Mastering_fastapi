from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# this funct is used to make the password irreversible hashed password

def hash(password : str):
    return pwd_context.hash(password)


# this funct verify whether the stored hashed password and the password which will , to check , been hashed are equal or not

def verify_hashed_passwords(plain_password , hashed_password):
    return pwd_context.verify(plain_password , hashed_password)