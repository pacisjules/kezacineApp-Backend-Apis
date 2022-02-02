from configs.connection import database
from db.table import users
from fastapi import APIRouter, HTTPException, Depends
from auth import model
from utils import util, constant
import uuid, datetime

import smtplib
import random
import string

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()






@router.post("/auth/register", response_model=model.UserList)
async def register(user: model.UserCreate):
    userDB = await util.findExistedUser(user.username)

    if userDB:
        raise HTTPException(status_code=400, detail="Username already existed")

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    #Randoming Password

    p1=random.choice(string.ascii_letters)
    p2=random.choice(string.ascii_letters)
    p3=random.choice(string.ascii_letters)
    p4=random.randint(111, 999)
    random_password=p1+p2+p3+str(p4)

    #End of Randoming Password

    query = users.insert().values(
        id = gid,
        username = user.username,
        password = util.get_password_hash(random_password),
        fullname = user.fullname,
        email = user.email,
        type = user.type,
        role = user.role,
        company= user.company,   
        phone= user.phone,    
        living= user.living,
        created_at = gdate,
        last_update_at = gdate,
        status = "1"
    )

        #Send Confirmation Email to this user

    #Auth
    sender="appsendertestv1@gmail.com"
    Email_password=str("Ishimwe@12")

    #Information
    me="Barnabs Software"
    subject="Account Confirmation!"
    receiver=user.email

    #Text Message
    content=" here is your confirmation link, Click button below to Confirm your Account here "

    #Message
    message="""From:"""+me+""""<appsendertestv1@gmail.com>
    To: To """+receiver+""" <"""+user.email+"""> MIME-Version: 1.0
    Content-type: text/html
    Subject: """+subject+"""

    """"Hallo "+user.fullname+" your password is "+random_password+content+" https://www.google.com/search?client=opera&q=goog&sourceid=opera&ie=UTF-8&oe=UTF-8"+"""
    """
    server=smtplib.SMTP("smtp.gmail.com", 587)

    #Start server & Login
    server.starttls()
    server.login(sender,Email_password)
    print("Login Success")

    #Send Email
    server.sendmail(sender, receiver, message)
    print("Email Sent")
    print(random_password)

    #End Confirmation Email


    await database.execute(query)
    return {
        **user.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }






@router.post("/auth/login", response_model=model.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    userDB = await util.findExistedUser(form_data.username)
    if not userDB:
        raise HTTPException(status_code=404, detail="User not found")

    user = model.UserPWD(**userDB)
    isValid = util.verify_password(form_data.password, user.password)
    
    if not isValid:
        raise HTTPException(status_code=404, detail="Incorrect username or password")

    access_token_expires = util.timedelta(minutes=constant.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = util.create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires,
    )

    results = {
        "access_token": access_token, 
        "token_type": "bearer",
        "expired_in": constant.ACCESS_TOKEN_EXPIRE_MINUTES*60,
        "user_info": user
    }

    return results