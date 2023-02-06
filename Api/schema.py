import motor.motor_asyncio
import uuid
from dotenv import load_dotenv
from bson import ObjectId
from pydantic import BaseModel,Field,EmailStr
import  os
#load env
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URI"))

db= client.blog_api




class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name:str = Field(...)
    email:EmailStr=Field(...)
    password:str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders ={ObjectId:str}
        schema_extra = {
            "example":{
            "name":"john doe",
            "email":"oluwatomisin",
            "password":"oluwatomisin"

            }
        }
class UserResponse(BaseModel):

    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name:str = Field(...)
    email:EmailStr=Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoder ={ObjectId:str}
        schema_extra = {
            "example":{
            "name":"john doe",
            "email":"oluwatomisin",
            
            }
        }

