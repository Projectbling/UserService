from tortoise.models import Model
from tortoise import fields
from Utility.GenerateUniqueCode import GenerateUniqueCode
#create interface model
class IBaseModel(Model):
    id = fields.BigIntField(pk=True, generated=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    isDeleted = fields.BooleanField(default=False)

    
        
        
    class Meta:
        abstract = True

class User(IBaseModel):
    
    
    email = fields.CharField(max_length=128, unique=True)
    refUserID=fields.BigIntField(default=0)
    referanceCode=fields.CharField(max_length=128, unique=True)

    
    def __init__(self, email, refUserID=0):
        super().__init__()
        
        self.email = email
        self.refUserID = refUserID
        self.referanceCode = GenerateUniqueCode.generateRandomCode(8)

  
    class Meta:
        table = "user"