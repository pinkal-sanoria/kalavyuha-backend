from pydantic import BaseModel,Field
from Utils.GenerateNumber import generateRandomNumber
from typing import Optional

class BusinessDetailsModel(BaseModel):
    ID : Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    BussinessUserId: int
    BusinessName: str
    ProfileImage: str
    Introduction: Optional[str] = None
    ShopName: str
    StreetAddress: str
    Nearby: Optional[str]
    ZipCode: str
    CityState: str
