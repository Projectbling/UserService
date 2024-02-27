from core.mediator import *
from typing import Annotated
from .schema import UserCreateSchema
from tortoise.transactions import in_transaction

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import Depends

from .model import User 
from Config.DatabaseConfig import DB_Context

@Mediator.handler("main")
class UserCreateHandler(MediatorBaseHandler):
    
    async def handle( req: UserCreateSchema):
        print(req.email)

        db = await DB_Context.get_db()
        
        user = User(email=req.email)
        db.add(instance=user)
        await db.commit()
        await db.refresh(user)
        db.close()
        return user



@Mediator.handler("test")
class TestUserCreateHandler(MediatorBaseHandler):
    async def handle(req:UserCreateSchema):
        print(req.email)
        user = User(email=req.email)
                
                  
            
        return await user 
               
