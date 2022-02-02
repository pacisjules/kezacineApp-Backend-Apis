from fastapi import APIRouter, Depends
from auth import model
from utils import util
from db.table import users
from configs.connection import database
from fastapi_pagination import Page, paginate
import uuid, datetime

router = APIRouter()

#Current User
@router.get("/users/me", response_model=model.UserList)
async def read_user_me(currentUser: model.UserList = Depends(util.get_current_active_user)):
    return currentUser

#find all users
@router.get("/users", response_model=Page[model.UserList])
async def find_all_user(
    currentUser: model.UserList = Depends(util.get_current_active_user)
):
    query = "select * from users"
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#Find one User by ID
@router.get("/users/{User_id}", response_model=model.UserList)
async def find_user_by_id(User_id: str, currentUser: model.UserList = Depends(util.get_current_active_user)):
    query = users.select().where(users.c.id == User_id)
    return await database.fetch_one(query)


#Update User
@router.put("/auth/update", response_model=model.UserListforUpdate)
async def update_user(user: model.UserUpdate, currentUser: model.UserList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = users.update().where(users.c.id == user.id).values(
        id = gid,
        username = user.username,
        password = util.get_password_hash(user.password),
        fullname = user.fullname,
        email = user.email,
        type = user.type,
        role = user.role,
        company= user.company,   
        phone= user.phone,    
        living= user.living,
        last_update_at = gdate,
        status = user.status
    )

    await database.execute(Query)
    return await find_user_by_id(user.id)



#Delete User
@router.delete("/users/{User_id}", response_model=model.UserList)
async def Delete_by_id(User_id: str, currentUser: model.UserList = Depends(util.get_current_active_user)):
    query = users.delete().where(users.c.id == User_id)
    return await database.execute(query)



#Account Confirmation
@router.put("/NewAccount/account_confirmation", response_model=model.UserListforUpdate)
async def update_user(user: model.UserUpdate):

    #gid = str(uuid.uuid1())

    gdate = str(datetime.datetime.now())

    Query = users.update().where(users.c.id == user.id).values(
        last_update_at = gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_user_by_id(user.id)