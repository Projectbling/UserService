from typing import Optional
from pydantic import BaseModel
from .model import User



#TODO: bunu silince çalışıyor mu?
class BaseModel(BaseModel):
    class Config:
        
        from_attributes=True


    



class UserCreateResponse(User):
    class Config:
        orm_mode = True
    