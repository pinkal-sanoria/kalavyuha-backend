from pydantic import BaseModel,Field
from Utils.GenerateNumber import generateRandomNumber
from typing import Optional,List

class ServiceInfoModel(BaseModel):
    ID : Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    BussinessId : int 
    ServiceName: str
    Price: float
    Duration: str  # Assuming the duration is given as a string like "30 mins", "1 day", etc.
    AssignedStaffs: Optional[str]  # In case no staff is assigned initially
    ServiceImage: Optional[List[str]]
