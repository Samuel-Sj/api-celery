from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi import Depends
from jose import JWTError, jwt
from pymongo.asynchronous.database import AsyncDatabase
from app.core.database import get_mongo_connection
from app.utils.utils import verify_password
import os
from dotenv import load_dotenv
load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user(username:str, db: AsyncDatabase):
    return await db["users"].find_one({"username":username})

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncDatabase = Depends(get_mongo_connection("users")),
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        username = payload.get("sub")
    except JWTError:
        raise credentials_exception

    if not username:
        raise credentials_exception

    user = await get_user(username=username, db=db)
    if not user:
        raise credentials_exception

    return user

async def authenticate_user(db: AsyncDatabase, username: str, password: str):
    user = await get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user

