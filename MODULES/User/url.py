from fastapi import APIRouter,Depends,Request
from tortoise.contrib.fastapi import HTTPNotFoundError
from .responce import UserCreateResponse
from tortoise.transactions import in_transaction
from .model import User 
from .schema import UserCreateSchema
from core.mediator import Mediator
guest_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not Found","model": HTTPNotFoundError} },
)





@guest_router.post("/register")
async def create_user(data: UserCreateSchema):
    return await Mediator.handle("main",data)

# @router.get("/{user_id}", response_model=UserOut)
# async def read_user(user_id: int):
#     return await UserService.get_user_by_id(user_id)
