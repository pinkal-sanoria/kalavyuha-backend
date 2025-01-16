from pydantic import BaseModel
from .BussinessMember import BusinessMemberModel
from .BusinessDetails import BusinessDetailsModel
from Core.Entities.Bussiness.BussinessStaff import StaffModel
from Core.Entities.Bussiness.BussinessService import ServiceInfoModel
from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class BusinessCompleteDetailsResponse(BaseModel):
    # business_member: Optional[BusinessMemberModel] = None
    BusinessDetails: Optional[BusinessDetailsModel] = None
    StaffDetails: Optional[StaffModel] = None
    Services: Optional[ServiceInfoModel] = None
