from pydantic import BaseModel
from typing import Optional, List
from Core.Models.DIscountProviderEnum import DiscountProviderEnum


class ProductInfoModel(BaseModel):
    BussinessId: int
    Name: str
    Price: float
    ImageURL : Optional[List[str]] = None
    isDiscount : Optional[bool] = False
    DiscountProvider : Optional[DiscountProviderEnum] =None # make enum -> BussinessOwner, Credit Card, Company
    StockCount : int
    DiscountPercentage : Optional[float] = None  # Allow null when no discount is applie

    @property
    def DiscountedPrice(self):
        """Calculate discounted price if discount is active."""
        if self.isDiscount and self.DiscountPercentage:
            return self.Price * (1 - self.DiscountPercentage / 100)
        return self.Price

