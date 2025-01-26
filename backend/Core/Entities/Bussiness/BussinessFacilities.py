from pydantic import BaseModel
from typing import Optional

class BusinessAmenitiesModel(BaseModel):
    BussinessId : int
    Accessibility: Optional[bool] = False
    InstantConfirmation: Optional[bool] = False
    Internet: Optional[bool] = False
    Parking: Optional[bool] = False
    Water: Optional[bool] = False
    ACCooler: Optional[bool] = False  # AC or Cooler
    ChildFriendly: Optional[bool] = False
