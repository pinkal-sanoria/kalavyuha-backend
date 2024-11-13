from pydantic import BaseModel
from typing import Optional
from datetime import  time

class AvailabilityModel(BaseModel):
    Day: str
    StartTime: time
    EndTime: time
    BreakTime: Optional[time]