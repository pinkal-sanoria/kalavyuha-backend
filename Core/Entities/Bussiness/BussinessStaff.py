from pydantic import BaseModel,Field
from typing import List
from typing import Optional,List
from Utils.GenerateNumber import generateRandomNumber

class TeamPresenceModel(BaseModel):
    Id: Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    
    staff_members: int
    staff_name: str
    staff_profile_image: str
    exp: int  # Assuming 'exp'(2) is experience in years
    role: str
