from fastapi import APIRouter,Depends,Request
from tortoise.contrib.fastapi import HTTPNotFoundError
from .responce import UserCreateResponse
from tortoise.transactions import in_transaction
from .schema import UserRegisterSchema
from .model import User 


guest_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not Found","model": HTTPNotFoundError} },
)


async def register_user(data: UserRegisterSchema) -> UserCreateResponse:
        print(data.email)
        async with in_transaction():
            user = await User.create(
                email=data.email,
                  
            )
            return await user


@guest_router.post("/register")
async def create_user(data: UserRegisterSchema):
    return await register_user(UserRegisterSchema(email=data.email))

# @router.get("/{user_id}", response_model=UserOut)
# async def read_user(user_id: int):
#     return await UserService.get_user_by_id(user_id)
