from fastapi import APIRouter, Depends
from Core.Models.Bussiness.BussinessRequestsModel import VerifyEmailOtpRequest
from Utils.EmailVerifcation import emailVerifcation
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.Customer.RequestBodyModel import VerifyOtpRequest
from Services.VerifyOtp import otpVerification
from Core.Models.ResultModel import Result
from Services.SendOTP import sendOtpMethod
from Core.Entities.MobileOTP import MobileOTPModel

OtpProcessRouter = APIRouter()


# OTP Verification API
@OtpProcessRouter.post("/send")
def sendOtp(request_body: MobileOTPModel) -> Result:
    # if tokenData is not True:
    #     return Result(Status=401, Message="Token is Not valid")
    return sendOtpMethod(request_body)


# OTP Verification API
@OtpProcessRouter.post("/verify")
def customerVerifyOtp(request_body: VerifyOtpRequest) -> Result:
    # if tokenData is not True:
    #     return Result(Status=401, Message="Token is Not valid")
    otp = request_body.OTP
    phoneNumber = request_body.PhoneNumber
    return otpVerification(otp, phoneNumber)


# API  to verify the Email
@OtpProcessRouter.post("/create/")
def emailOtpVerify(
    request_body: VerifyEmailOtpRequest, tokenData: bool = Depends(tokenRequiredCheck)
) -> Result:
    if tokenData is not True:
        return Result(Status=401, Message="Token is Not valid")
    otp = request_body.otp
    email = request_body.Email
    return emailVerifcation(otp, email)
