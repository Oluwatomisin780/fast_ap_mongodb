from fastapi import APIRouter,HTTPException,status
from fastapi.encoders import  jsonable_encoder
from schema import User,db,UserResponse
from utils import get_password_hash,verify_password
from send_email import send_registration_mail
import secrets
router =  APIRouter(
    tags=["User Routes"]
)


@router.get('/')
def get():
    return {"message":"Hello world!"}

@router.post('/registeration',response_description="Register User",response_model=UserResponse)
async def register_user(user_info:User):
    user_info = jsonable_encoder(user_info)
    #check for duplication
    user_found= await db["Users"].find_one({
        "name":user_info["name"]
    })

    email_exist = await db['Users'].find_one({
        "email":user_info["email"]
    })

    if user_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail= 'username is already taken')
    if email_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='email already exist')
    #hash password
    user_info["password"] =  get_password_hash(user_info["password"])
    #create api key
    user_info["apiKey"] = secrets.token_hex(30)

    new_user = await db["Users"].insert_one(user_info)
    created_user = await db["Users"].find_one({"_id":new_user.inserted_id})

    #user email verification
    await send_registration_mail("Registeration sucessful", user_info["email"],{
        "title": "Registration sucessful",
        "name":user_info["name"]
    })
    return created_user