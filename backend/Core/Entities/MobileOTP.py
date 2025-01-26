from pydantic import BaseModel, Field
from Utils.GenerateNumber import generateRandomNumber
from typing import Optional


class MobileOTPModel(BaseModel):
    ID: Optional[int] = Field(default=generateRandomNumber(), alias="_id")
    PhoneNumber: str
    OTP: Optional[int] = None
    UserType: Optional[str] = None
