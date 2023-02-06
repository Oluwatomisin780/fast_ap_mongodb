from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import  OAuth2PasswordRequestForm
from schema import db
from oauth2 import access_token 

import utils
router =  APIRouter(
    prefix="/login",
    tags= ["Authentication"]
)

@router.post("",status_code=status.HTTP_200_OK)
async def login(user_credentials:OAuth2PasswordRequestForm=Depends()):
    user = await db["Users"].find_one({"name":user_credentials.username})


    if user and utils.verify_password(user_credentials.password,user["password"]):
        accessToken = access_token({"id":user["_id"]})

        return ({"acess_token":accessToken, "token_type":"bearer"})
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid User Cedentials")