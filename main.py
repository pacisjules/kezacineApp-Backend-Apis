from configs.connection import database
from fastapi import FastAPI, Depends, Request
from functools import lru_cache
from configs import appinfo
import time
from fastapi_pagination import add_pagination

app = FastAPI()

@lru_cache()
def app_setting():
    return appinfo.Setting()

@app.get("/", tags=["Root"])
async def root():
    return{
        "message": "This Apis for Movies Streaming Platform"
    }

@app.get("/app/info", tags=["App"])
async def app_info():
    return {
        "app_name"      : "Keza Cine Movies Streaming Platform",
        "app_version"   : "1.0",
        "app_framework" : "FastAPI (Python)",
        "app_date"      : "2021-01-01 20:48:10",
        "owner_name"    :"ISHIMWE JULES Pacis",
    }

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)

    return response

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

from auth import controller as authController
from users import controller as userController
from customer import controller as customerController





#Config Parts
app.include_router(authController.router, tags=["Auth"])
app.include_router(userController.router, tags=["Users"])
app.include_router(customerController.router, tags=["Customers"])



add_pagination(app)