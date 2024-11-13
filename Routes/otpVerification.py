from fastapi import APIRouter
from Core.Models.Customer.RequestBodyModel import VerifyOtpRequest
from Services.VerifyOtp import otpVerification

VerifyOtp = APIRouter()

@VerifyOtp.post("/")
def customerVerifyOtp(request_body: VerifyOtpRequest):
    otp = request_body.otp
    userId = request_body.UserId
    return otpVerification(otp, userId)

