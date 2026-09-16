from pydantic import BaseModel

class User (BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_type:str
    token_type: str