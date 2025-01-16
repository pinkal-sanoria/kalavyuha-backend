from pydantic import BaseModel, Field
from Utils.GenerateNumber import generateRandomNumber
from typing import Optional
from Core.Models.Bussiness.BusinessRole import BusinessRole
from datetime import datetime
from zoneinfo import ZoneInfo

class BusinessDetailsModel(BaseModel):
    ID: Optional[int] = Field(default=generateRandomNumber(), alias="_id")
    BussinessUserId: int
    BussinessType: BusinessRole
    BusinessName: str
    ProfileImage: str
    Introduction: Optional[str] = None
    ShopNumber: Optional[str] = None
    StreetAddress: str
    Nearby: Optional[str]
    ZipCode: str
    Region : str #city state name
    Latitude: float  # Latitude as a float
    Longitude: float  # Longitude as a float
    LikesCount : int
    website: Optional[str] = Field(default=None, description="User's website")
    OpeningTime: str = Field(..., description="Opening time in HH:MM format")
    ClosingTime: str = Field(..., description="Closing time in HH:MM format")
    CreatedOn: datetime = datetime.now(ZoneInfo("Asia/Kolkata"))
    CreatedBy: Optional[int] = None
    UpdatedOn: datetime = datetime.now(ZoneInfo("Asia/Kolkata"))
    UpdatedBy: Optional[int] = None


class BusinessDetailsUpdateModel(BaseModel):
    BusinessName: Optional[str] = None
    ProfileImage: Optional[str] = None
    Introduction: Optional[str] = None
    ShopName: Optional[str] = None
    StreetAddress: Optional[str] = None
    Nearby: Optional[str] = None
    ZipCode: Optional[str] = None
    CityState: Optional[str] = None
    BussinessRole: Optional[str] = None
    website: Optional[str] = None
