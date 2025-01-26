from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from pytz import timezone
import uuid


class ReviewsModel(BaseModel):
    ReviewId: Optional[str] = Field(default_factory=lambda: str(uuid.uuid1()))  # Unique ID for the review
    UserId: str  # Foreign key to link with the Customer model's UserId
    Name: str  # Reviewer's name
    Rating: float  # Star rating (e.g., 4.5)
    ReviewText: str  # Review content
    CreatedOn: datetime = datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S.%f")  # Timestamp of creation
    IsActive: bool = True  # Flag to mark review as active/inactive