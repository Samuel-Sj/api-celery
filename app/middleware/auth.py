from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi import Depends
from jose import JWTError, jwt
from pymongo.asynchronous.database import AsyncDatabase
from app.core.database import get_mongo_connection
from app.utils.utils import verify_password
import os
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user(username:str, db: AsyncDatabase):
    return await db["users"].find_one(username)

async def get_current_user(username:str, db: AsyncDatabase, token: str = Depends(oauth2_scheme)):
    user = await db["users"].find_one({"username":username})
    if not user or user is None:
        raise HTTPException(status_code=401,detail="Não foi possível validar as credenciais",headers={"WWW-Authenticate":"Bearer"})

    try:
        payload = jwt.decode(token=token,key=os.getenv("SECRET_KEY"),algorithms="HS256")
    except JWTError:
        raise HTTPException(status_code=401,detail="Erro JWT")

    return user

async def authenticate_user(db: AsyncDatabase, username: str, password: str):
    user = await get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

