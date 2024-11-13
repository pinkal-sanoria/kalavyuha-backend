from fastapi import APIRouter
from Core.Entities.Customer.Customer import Customer
from Services.Customer.CreateCustomerUser import createNewCustomerAccount

CustomerSignUp = APIRouter()

@CustomerSignUp.post("/create/")
def customerSignUp(member: Customer):
    return createNewCustomerAccount(member)
