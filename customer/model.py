from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    user_id: str = Field(..., example="user id")
    institution_id:str =  Field(..., example="Instition Id")
    company_name: str = Field(..., example="company name")
    tin_number: str = Field(..., example="TIN NUMBER")
    represent_names: str = Field(..., example="Represent names")
    address1: str = Field(..., example="Address1")
    address2: str = Field(..., example="Address2")
    province: str = Field(..., example="Province")
    district: str = Field(..., example="District")
    phone1:str = Field(..., example="Phone1")
    phone2:str = Field(..., example="Phone2")
    email: str    = Field(..., example="email@gmail.com")


class CustomerList(BaseModel):
    id: str
    user_id: str
    institution_id: str
    company_name: str
    tin_number: str
    represent_names: str
    address1: str 
    address2: str 
    province: str 
    district: str 
    phone1:str 
    phone2:str
    email: str 
    status: str
    created_at: str
    last_update_at: str


class CustomerUpdate(BaseModel):
    id: str
    user_id: str
    institution_id: str
    company_name: str
    tin_number: str
    represent_names: str
    address1: str 
    address2: str 
    province: str 
    district: str 
    phone1:str 
    phone2:str
    email: str 
    status: str
    last_update_at: str
