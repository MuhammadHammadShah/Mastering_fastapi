# from dotenv import dotenv_values , load_dotenv
# import os

# load_dotenv()
# # Load .env file
# print(os.getenv('ALGORITHM'))

































# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print("ENV FILE LOADED")
# print(f"database_hostname: {os.getenv('database_hostname')}")
# print(f"database_port: {os.getenv('database_port')}")
# print(f"database_password: {os.getenv('database_password')}")
# print(f"database_name: {os.getenv('database_name')}")
# print(f"database_username: {os.getenv('database_username')}")
# print(f"secret_key: {os.getenv('secret_key')}")
# print(f"algorithm: {os.getenv('algorithm')}")
# print(f"access_token_expire_minutes: {os.getenv('access_token_expire_minutes')}")

# class Settings(BaseSettings):
#     database_hostname: str
#     database_port: int
#     database_password: str
#     database_name: str
#     database_username: str
#     secret_key: str
#     algorithm: str
#     access_token_expire_minutes: int

#     class Config:
#         env_file = ".env"

# settings = Settings()
# print("Settings loaded successfully")
