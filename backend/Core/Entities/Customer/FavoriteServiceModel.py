from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from pytz import timezone
import uuid


class FavoriteServiceModel(BaseModel):
    UserId: int  # Foreign key to link to the Customer model's UserId
    BussinessId: int  # Foreign key to link to the ServiceInfoModel's ServiceID
    AddedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S.%f")  # Timestamp
