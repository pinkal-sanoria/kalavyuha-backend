from enum import Enum

class DiscountProviderEnum(str, Enum):
    BUSINESS_OWNER = "BusinessOwner"
    CREDIT_CARD = "CreditCard"
    COMPANY = "Company"
