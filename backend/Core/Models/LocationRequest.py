from pydantic import BaseModel

# Make the location Request
class LocationRequest(BaseModel):
    Latitude: float
    Longitude: float
