from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    email: EmailStr
    






