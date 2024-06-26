from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQL_DATABASE_URL = 'postgresql://postgres:POSTGRESforPIAIC.6/11/2024@localhost/fastapi_db'

engine = create_engine(SQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False , autoflush= False , bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost' , database='fastapi_db' , user='postgres' , password='POSTGRESforPIAIC.6/11/2024' , cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection was Successfull! ")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: " , error)
#         time.sleep(4)
