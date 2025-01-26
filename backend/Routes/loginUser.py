from fastapi import APIRouter, Depends
from Core.Models.Customer.RequestBodyModel import UserLoginRequest
from Services.Customer.LoginCustomer import loginCustomer
from Services.Bussiness.Create.BussinessUserLogin import loginMerchant
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result

UserLogin = APIRouter()


# ApI To Login Customer
@UserLogin.post("/customer/")
def customerLogin(RequestBody: UserLoginRequest) -> Result:
    return loginCustomer(RequestBody)


# ApI To Login Merchant
@UserLogin.post("/Merchant/")
def merchantLogin(RequestBody: UserLoginRequest) -> Result:
    return loginMerchant(RequestBody)
