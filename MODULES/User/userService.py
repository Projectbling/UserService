from core.mediator import *
from .schema import UserCreateSchema
from tortoise.transactions import in_transaction

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends
from Config.DatabaseConfig import DB_Context
from .model import User 


@Mediator.handler("main")
class UserCreateHandler(MediatorBaseHandler):
    async def handle(self, req: UserCreateSchema, db: AsyncSession = Depends(DB_Context.get_db)):
        print(req.email)
        user = User(email=req.email)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user



@Mediator.handler("test")
class TestUserCreateHandler(MediatorBaseHandler):
    async def handle(req:UserCreateSchema):
        print(req.email)
        user = User(email=req.email)
                
                  
            
        return await user 
               
