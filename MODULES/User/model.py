


from sqlalchemy import Column, Integer, String, DateTime, Boolean, Sequence
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import random
from Utility.GenerateUniqueCode import GenerateUniqueCode

class Base(DeclarativeBase):
    pass


class IBaseModel(Base):
    __abstract__ = True
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    isDeleted = Column(Boolean, default=False)

class User(IBaseModel):
    
    __tablename__ = 'user'

    email = Column(String(128), unique=True)
    refUserID = Column(Integer, default=0)
    referanceCode = Column(String(128), unique=True)

    def __init__(self, email, refUserID=0):
        
        self.email = email
        self.refUserID = refUserID
        self.referanceCode = GenerateUniqueCode.generateRandomCode(8)



  










#create interface model
# class IBaseModel(Model):
#     id = fields.BigIntField(pk=True, generated=True)
#     created_at = fields.DatetimeField(auto_now_add=True)
#     updated_at = fields.DatetimeField(auto_now=True)
#     isDeleted = fields.BooleanField(default=False)

    
        
        
#     class Meta:
#         abstract = True

# class User(IBaseModel):
    
    
#     email = fields.CharField(max_length=128, unique=True)
#     refUserID=fields.BigIntField(default=0)
#     referanceCode=fields.CharField(max_length=128, unique=True)

    
#     def __init__(self, email, refUserID=0):
#         super().__init__()
        
#         self.email = email
#         self.refUserID = refUserID
#         self.referanceCode = GenerateUniqueCode.generateRandomCode(8)

  
#     class Meta:
#         table = "user"