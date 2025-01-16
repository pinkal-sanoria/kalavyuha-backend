from pydantic import BaseModel, Field
from typing import Optional
import uuid
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime
from pytz import timezone


# Create Account
class BusinessMemberModel(BaseModel):
    ID: Optional[int] = Field(default=generateRandomNumber(), alias="_id")
    FirstName: str
    LastName: str
    Email: Optional[str]
    PhoneNumber: str
    Password: str
    # Latitude: Optional[float] = Field(default=None, description="Latitude coordinate")
    # Longitude: Optional[float] = Field(default=None, description="Longitude coordinate")
    # IpAddress: Optional[str] = Field(default=None, description="User's IP address")
    isActive: Optional[bool] = True
    isVerified: Optional[bool] = False
    isDeleted: Optional[bool] = False
    isAgree: Optional[bool] = Field(default=False, description="User agreement status")
    CreatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    CreatedBy: Optional[int] = None
    UpdatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    UpdatedBy: Optional[int] = None
   

class BusinessMemberUpdateModel(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Password: Optional[str] = None
    isActive: Optional[bool] = None
    isVerified: Optional[bool] = None
    isDeleted: Optional[bool] = None
    is_agree: Optional[bool] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    ip_address: Optional[str] = None
    UpdatedBy: Optional[int] = None
