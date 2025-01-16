from pydantic import BaseModel, Field
from typing import List
from typing import Optional, List
from Utils.GenerateNumber import generateRandomNumber

class StaffModel(BaseModel):
    Id: Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    StaffNumber: int
    StaffNumber: int
    ProfileImage: str
    Experience: str  # Assuming 'exp'(2) is experience in years
    Role: str
    Specialization : str


class TeamPresenceUpdateModel(BaseModel):
    staff_members: Optional[int] = None
    staff_name: Optional[str] = None
    staff_profile_image: Optional[str] = None
    exp: Optional[int] = None
    role: Optional[str] = None