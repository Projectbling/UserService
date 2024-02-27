from core.mediator import *
from .schema import UserCreateSchema
from tortoise.transactions import in_transaction

from .model import User 


@Mediator.handler("main")
class UserCreateHandler(MediatorBaseHandler):
    async def handle(req:UserCreateSchema):
        print(req.email)
        async with in_transaction():
            user = await User.create(
                email=req.email,
                  
            )
            return await user
    
