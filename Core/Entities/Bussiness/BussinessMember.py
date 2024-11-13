from pydantic import BaseModel,Field
from typing import Optional
import uuid
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime
from pytz import timezone

# Create Account
class BusinessMemberModel(BaseModel):
    ID : Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    BussinessId: Optional[str] = Field(default_factory=lambda: str(uuid.uuid1()))
    UserId : Optional[str] = "bussiness123"
    FirstName: str 
    LastName: str
    Email: Optional[str] 
    PhoneNumber: str
    Password: str
    Otp: Optional[int] = None
    isActive : Optional[bool]= True
    isVerified : Optional[bool] = True
    isDeleted : Optional[bool] = True
    CreatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime( "%Y-%m-%d %H:%M:%S.%f")
    CreatedBy: Optional[int] = None
    UpdatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime( "%Y-%m-%d %H:%M:%S.%f")
    UpdatedBy: Optional[int] = None
