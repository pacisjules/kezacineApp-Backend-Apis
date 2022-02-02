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



# Find customer with names
@router.get("/likecustomer/{names}", response_model=Page[model.CustomerList])
async def find_like_customer(names: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):

    query = "select * from customer where company_names like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)

#Find one Customer by ID
@router.get("/customer/{customer_id}", response_model=model.CustomerList)
async def find_customer_by_id(customer_id: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.id == customer_id)
    return await database.fetch_one(query)

#Find one Customer by TIN Number
@router.get("/customer_tin/{tin_number}", response_model=model.CustomerList)
async def find_customer_by_tin_number(tin_number: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.tin_number == tin_number)
    return await database.fetch_one(query)


# Find customers with institution id

@router.get("/all_customers_by_institution/{institu_id}", response_model=Page[model.CustomerList])
async def find_customers_by_institution(institu_id: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.institution_id == institu_id)
    res = await database.fetch_all(query)
    return paginate(res)


# Find customer with Phone Number

@router.get("/customer_by_phone_number/{phone}", response_model=Page[model.CustomerList])
async def find_customer_by_phone_number(phone: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.phone1 == phone) or customer.select().where(customer.c.phone2 == phone)
    res = await database.fetch_one(query)
    return paginate(res)



# Find customers by province
@router.get("/all_customers_by_province/{province}", response_model=Page[model.CustomerList])
async def find_customers_by_province(province: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.province == province)
    res = await database.fetch_all(query)
    return paginate(res)


# Find customers by district
@router.get("/all_customers_by_district/{district}", response_model=Page[model.CustomerList])
async def find_customers_by_district(district: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.district == district)
    res = await database.fetch_all(query)
    return paginate(res)



# Find customers by email
@router.get("/customer_by_email/{email}", response_model=Page[model.CustomerList])
async def find_customer_by_email(email: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.email == email)
    res = await database.fetch_all(query)
    return paginate(res)


# Find customers by status
@router.get("/customer_by_status/{status}", response_model=Page[model.CustomerList])
async def find_customer_by_status(status: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.select().where(customer.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)



# Find customers by Represent
@router.get("/customer_by_representer/{names}", response_model=Page[model.CustomerList])
async def find_like_representer(names: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):

    query = "select * from customer where represent_names like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)

# add new customer
@router.post("/addcustomer", response_model=model.CustomerList)
async def registerCustomer(cstm: model.CustomerCreate, currentUser: model.CustomerList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = customer.insert().values(
        id = gid,
        user_id=cstm.user_id,
        institution_id=cstm.institution_id,
        company_name = cstm.company_name,
        tin_number =cstm.tin_number,
        represent_names= cstm.represent_names,
        address1= cstm.address1 ,
        address2= cstm.address2 ,
        province= cstm.province ,
        district= cstm.district ,
        phone1=cstm.phone1 ,
        phone2=cstm.phone2,
        email=cstm.email,
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
        user_id=cstm.user_id,
        institution_id=cstm.institution_id,
        company_name = cstm.company_name,
        tin_number =cstm.tin_number,
        represent_names= cstm.represent_names,
        address1= cstm.address1 ,
        address2= cstm.address2 ,
        province= cstm.province ,
        district= cstm.district ,
        phone1=cstm.phone1 ,
        phone2=cstm.phone2,
        email=cstm.email,
        last_update_at = gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_customer_by_id(cstm.id)


#Delete Customer
@router.delete("/Delete_Customer/{Customer_id}", response_model=model.CustomerList)
async def Delete_by_Customer_id(Customer_id: str, currentUser: model.CustomerList = Depends(util.get_current_active_user)):
    query = customer.delete().where(customer.c.id == Customer_id)
    return await database.execute(query)