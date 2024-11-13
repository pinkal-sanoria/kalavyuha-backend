from pydantic import BaseModel

class BusinessSignupRequest(BaseModel):
    FirstName: str
    LastName: str
    EMail: str
    Phone: str
    Password: str

class VerifyEmailOtpRequest(BaseModel):
    Email: str
    otp: int