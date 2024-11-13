from pydantic import BaseModel,Field
from typing import Optional
from Utils.GenerateNumber import generateRandomNumber
import uuid
from datetime import datetime
from pytz import timezone


class Customer(BaseModel):
    ID : Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    UserId: Optional[str] = Field(default_factory=lambda: str(uuid.uuid1()))
    Name: str
    Username: str
    Email: Optional[str] = None
    PhoneNumber: str
    Password: str
    Otp: Optional[int] = None
    IsVerified: bool = False
    LastLogin: Optional[datetime] = None
    IsActive: bool = True
    IsDeleted: bool = False
    CreatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime( "%Y-%m-%d %H:%M:%S.%f")
    CreatedBy: Optional[int] = None
    UpdatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime( "%Y-%m-%d %H:%M:%S.%f")
    UpdatedBy: Optional[int] = None
