from pydantic import BaseModel, Field
from typing import Optional
from Utils.GenerateNumber import generateRandomNumber
import uuid
from datetime import datetime
from enum import Enum
from pytz import timezone


class Role(str, Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"
    MERCHANT = "Merchant"


class UserCredentails(BaseModel):
    ID: Optional[int] = Field(default=generateRandomNumber(), alias="_id")

    UserId: Optional[int] = Field(default_factory=lambda: str(uuid.uuid1()))

    UserRole: Role

    Token: str

    CreationTime: datetime

    ExpiredTime: Optional[datetime] = None

    IsValid: Optional[bool] = True

    CreatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    CreatedBy: Optional[int] = None

    UpdatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    UpdatedBy: Optional[int] = None
