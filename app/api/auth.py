from fastapi import APIRouter,Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models.User import User,Token
from app.core.database import get_mongo_connection
from pymongo.asynchronous.database import AsyncDatabase
from app.middleware.auth import authenticate_user, get_user, get_current_user
from app.utils.utils import create_access_token,get_password_hash

router = APIRouter()

@router.post("/token",response_model=Token)
async def login_for_access_token(form_Data: OAuth2PasswordRequestForm = Depends(),db: AsyncDatabase = Depends(get_mongo_connection("users"))):
    user = await authenticate_user(db=db,username=form_Data.username,password=form_Data.password)
    if not user or user is None:
        raise HTTPException(status_code=401, detail="Não foi possível validar as credenciais",headers={"WWW-Authenticate":"Bearer"})

    access_token = create_access_token(data={"sub":user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login",response_model=User)
async def login (user: User, db: AsyncDatabase = Depends(get_mongo_connection("users"))):
    db_user = await get_user(username = user.username,db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já registrado !")

    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username,password=hashed_password)
    await db["users"].insert_one(db_user.model_dump())
    return db_user

@router.get("/me")
async def me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"]}