from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi import Depends
from jose import JWTError, jwt
from pymongo.asynchronous.database import AsyncDatabase
from app.core.database import get_mongo_connection
from app.models.User import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_user(username:str, db: AsyncDatabase):
    user = await db["users"].find_one(username)
