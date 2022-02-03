from fastapi import APIRouter, HTTPException, Depends
from db.table import customer
from customer import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()

# All customers
@router.get("/all_customers", response_model=Page[model.CustomerList])
async def find_allcustomer(currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select()
    res = await database.fetch_all(query)
    return paginate(res)



# Find customers with country
@router.get("/likecustomer/{country}", response_model=Page[model.CustomerList])
async def find_like_customer(country: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):

    query = "select * from customer where country like '%{}%'".format(country)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#Find one Customer by ID
@router.get("/customer/{customer_id}", response_model=model.CustomerList)
async def find_customer_by_id(customer_id: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.id == customer_id)
    return await database.fetch_one(query)


# Find customers by ip_address
@router.get("/all_customers_by_district/{ip}", response_model=Page[model.CustomerList])
async def find_customers_by_district(ip: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.ip_address == ip)
    res = await database.fetch_all(query)
    return paginate(res)



# Find customers by status
@router.get("/customer_by_status/{status}", response_model=Page[model.CustomerList])
async def find_customer_by_status(status: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new customer
@router.post("/addcustomer", response_model=model.CustomerList)
async def registerCustomer(cstm: model.CustomerCreate):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = customer.insert().values(
        
        id = gid,
        country=cstm.country,
        code=cstm.code,
        ip_address=cstm.ip_address,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **cstm.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }


#Update Customer
@router.put("/customer_update", response_model=model.CustomerList)
async def update_customer(cstm: model.CustomerUpdate, currentUser: model.CustomerList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = customer.update().where(customer.c.id == cstm.id).values(
        id = gid,
        country=cstm.country,
        code=cstm.code,
        ip_address=cstm.ip_address,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_customer_by_id(cstm.id)


#Delete Customer
@router.delete("/Delete_Customer/{Customer_id}", response_model=model.CustomerList)
async def Delete_by_Customer_id(Customer_id: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.delete().where(customer.c.id == Customer_id)
    return await database.execute(query)