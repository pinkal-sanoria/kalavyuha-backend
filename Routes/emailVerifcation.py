from fastapi import APIRouter
from Core.Models.Bussiness.BussinessRequestsModel import VerifyEmailOtpRequest
from Utils.EmailVerifcation import emailVerifcation

EmailOtpVerify = APIRouter()

@EmailOtpVerify.post("/create/")
def emailOtpVerify(request_body:VerifyEmailOtpRequest):
    otp  = request_body.otp
    email = request_body.Email
    return emailVerifcation(otp,email)