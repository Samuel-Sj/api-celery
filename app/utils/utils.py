from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime,timedelta

import os

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def verify_password (plain_password:str, hashed_password) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password:str) -> str:
    return pwd_context.hash(password)

def create_access_token(data:dict, secret: str, expiren_in: int=3600):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(seconds=expiren_in)
    return jwt.encode(payload,os.getenv("SECRET_KEY"))