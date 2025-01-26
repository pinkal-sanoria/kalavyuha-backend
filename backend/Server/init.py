from fastapi import FastAPI
from Routes.signUpBussinessMember import BusinessMember
from Routes.createNewCustomerAccount import CustomerSignUp
from Routes. CustomerReview import CustomerReview
from Routes.FavoriteService import FavoriteService
from Routes.loginUser import UserLogin
from Routes.otpVerification import OtpProcessRouter
from Routes.signUpBusinessDetails import BusinessDetails
from Routes.signUpTeamPresence import Staff
from Routes.addServiceInfo import ServiceInfo
from Routes.addDocuments import Documents
from Routes.locationByPin import PincodeLocation
from Routes.Products import Products
from Routes.Facilities import Facilities
from Routes.businessCompleteDetails import BusinessCompleteDetailsRouter
# from Routes.emailVerifcation import EmailOtpVerify


app = FastAPI()

# BUSSINESS RELATED APIS
app.include_router(BusinessMember, prefix="/api/v1/BussinessMember")
app.include_router(OtpProcessRouter, prefix="/api/v1/otp")
app.include_router(BusinessDetails, prefix="/api/v1/BussinessDetails")
app.include_router(Staff, prefix="/api/v1/teamPresence")
app.include_router(ServiceInfo, prefix="/api/v1/Service")
app.include_router(Documents, prefix="/api/v1/Documents")
app.include_router(PincodeLocation, prefix="/api/v1/Pincode")
app.include_router(Products, prefix="/api/v1/products")
app.include_router(Facilities, prefix="/api/v1/facilities")

# CUSTOMER APIS
app.include_router(CustomerSignUp, prefix="/api/v1/customer/signUp")
app.include_router(UserLogin, prefix="/api/v1/login")
app.include_router(CustomerReview, prefix="/api/v1/CustomerReview")
app.include_router(FavoriteService, prefix="/api/v1/FavoriteService")

# app.include_router(TokenCreation, prefix="/api/v1/Documents")

# LOGIN
# app.include_router()
# Server/init.py


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}
