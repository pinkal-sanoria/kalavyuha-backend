from fastapi import APIRouter
from Core.Entities.Customer.Customer import Customer
from Services.Customer.CreateCustomerUser import createNewCustomerAccount
from Core.Models.ResultModel import Result

CustomerSignUp = APIRouter()


# Create Customer Account
@CustomerSignUp.post("/create/")
def customerSignUp(member: Customer) -> Result:
    return createNewCustomerAccount(member)
