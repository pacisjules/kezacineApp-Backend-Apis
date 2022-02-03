from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    
    country:str =  Field(..., example="Country Name")
    code: str = Field(..., example="Code")
    ip_address: str = Field(..., example="Ip Address")

class CustomerList(BaseModel):

    id: str
    country:str 
    code: str 
    ip_address: str 
    status: str
    created_at: str
    last_update_at: str

class CustomerUpdate(BaseModel):
    
    id: str
    country:str 
    code: str 
    ip_address: str 
    status: str
    created_at: str
    last_update_at: str
