from fastapi import FastAPI
from Routes.signUpBussinessMember import CreateBusinessMember
from Routes.createNewCustomerAccount import CustomerSignUp
from Routes.loginUser import CustomerLogin
from Routes.otpVerification import VerifyOtp
from Routes.signUpBusinessDetails import CreateBusinessDetails
from Routes.signUpTeamPresence import Staff
from Routes.addServiceInfo import CreateServiceInfo
from Routes.addBusinessRoleSelection import Documents
# from Routes.emailVerifcation import EmailOtpVerify

app = FastAPI()

# BUSSINESS RELATED APIS
app.include_router(CreateBusinessMember,prefix="/api/v1/BussinessMember")
app.include_router(VerifyOtp,prefix="/api/v1/verifyOtp")
app.include_router(CreateBusinessDetails,prefix="/api/v1/BussinessDetails")
app.include_router(Staff,prefix="/api/v1/teamPresence")
app.include_router(CreateServiceInfo,prefix="/api/v1/Service")
app.include_router(CreateServiceInfo,prefix="/api/v1/Services")
app.include_router(Documents,prefix="/api/v1/Documents")

# # CUSTOMER APIS
app.include_router(CustomerSignUp,prefix="/api/v1/customer/signUp")
app.include_router(CustomerLogin,prefix="/api/v1/customer/login")

