from pydantic import BaseModel


class UserSignupRequest(BaseModel):
    Name: str
    Username: str
    ContactNo: str
    Email: str
    Password: str


class UserLoginRequest(BaseModel):
    PhoneNumber: int
    Password: str


class VerifyOtpRequest(BaseModel):
    PhoneNumber: str
    OTP: int
