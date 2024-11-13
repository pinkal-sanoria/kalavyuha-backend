from fastapi import APIRouter
from Core.Models.Customer.RequestBodyModel import UserLoginRequest
from Services.Customer.LoginCustomer import loginUser

CustomerLogin = APIRouter()

@CustomerLogin.post("/")
def customerLogin(RequestBody: UserLoginRequest):
    return loginUser(RequestBody)


