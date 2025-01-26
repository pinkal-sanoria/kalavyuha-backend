from pydantic import BaseModel
from enum import Enum


# Enum to restrict the role selection to the 4 specific categories
class BusinessRole(str, Enum):
    beauty = "Beauty"
    wellness = "Wellness"
    fitness = "Fitness"
    healthcare = "Health Care"


class BusinessRoleSelectionModel(BaseModel):
    role: BusinessRole
