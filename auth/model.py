from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(..., example="manzo12")
    fullname: str = Field(..., example="Manzi Jacques")
    #password: str = Field(..., example="***")
    email: str    = Field(..., example="manzii5@gmail.com")
    type: str    = Field(..., example="Normal")
    role:str = Field(..., example="Manager")
    company: str    = Field(..., example="Company")
    phone: str    = Field(..., example="phone")
    living: str    = Field(..., example="Kigali")

class UserList(BaseModel):
    id: str
    username: str
    fullname: str
    email: str
    type: str 
    role:str
    company: str    
    phone: str    
    living: str 
    status: str
    created_at: str
    last_update_at: str


class UserListforUpdate(BaseModel):
    id: str
    username: str
    password: str
    fullname: str
    email: str
    type: str 
    role:str
    company: str    
    phone: str    
    living: str 
    status: str

class UserUpdate(BaseModel):
    id: str 
    username: str
    password: str 
    fullname: str 
    email: str 
    type: str 
    role:str
    company: str    
    phone: str   
    living: str
    status: str

class UserPWD(UserList):
    password: str

class Token(BaseModel):
    access_token: str
    token_type  : str
    expired_in  : str
    user_info   : UserList

class TokenData(BaseModel):
    username: str = None