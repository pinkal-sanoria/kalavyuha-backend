from pydantic import BaseModel
from typing import Optional, List


class ServiceInfoModel(BaseModel):
    BussinessId: int
    ServiceName: str
    Price: float
    Duration: (
        str  # Assuming the duration is given as a string like "30 mins", "1 day", etc.
    )
    AssignedStaffs: Optional[List[int]] = None  # In case no staff is assigned initially
    ImageURL : Optional[List[str]] = None
    isDiscount : Optional[bool] = False
    DiscountProvider : Optional[str] = None # make enum -> BussinessOwner, Credit Card, Company
    DiscountPercentage : Optional[float] = None  # Allow null when no discount is applie

    @property
    def DiscountedPrice(self):
        """Calculate discounted price if discount is active."""
        if self.isDiscount and self.DiscountPercentage:
            return self.Price * (1 - self.DiscountPercentage / 100)
        return self.Price

