from jose  import JOSEError,jwt
from  datetime import date,datetime,timedelta
from dotenv import load_dotenv
from typing import Dict
import os 
load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES  = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES ")
def access_token(payload:Dict):
    to_encode = payload.copy()

    expiration_time = datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({"exp":expiration_time})
    jw_token = jwt.encode(to_encode,key=str(os.getenv("SECRET_KEY ")),algorithm=os.getenv("ALGORITHM"))

    return jw_token
