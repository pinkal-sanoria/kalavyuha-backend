from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Entities.Customer import Customer
from Utils.HashPassword import hashPassword
from Utils.GenerateOtp import generateOtp
from Utils.SendOtp import sendOtpOnMobileNumber
from datetime import datetime
from Core.Models.CollectionEnum import collections
import uuid

# Create Customer Record
def createNewCustomerAccount(customerObj) -> Result:
    # try:
        mongoDb = MongoDBHandler()

        print(customerObj.dict(by_alias = True))
       
        # Check if the email already exists in the database
        existingMember = mongoDb.findDocument(collections.Customers.value,{"PhoneNumber": customerObj.PhoneNumber})
        
        if existingMember:
            return Result(Status=400,Message="User Already Exist")
        
        # Convert the model to a dictionary and insert it into MongoDB
        memberDict = customerObj.dict(by_alias = True)

        otp = generateOtp()

        memberDict["Otp"] = otp

        result = mongoDb.insertDocument(collections.BussinessMember.value,memberDict)
 
        sendOtpOnMobileNumber(otp,643564385684)       

        # Return a dictionary with the inserted ID
        return Result(Data=result.Data,Status=200,Message="Bussiness User Created Succesfully")


    # except Exception as ex:
    #     message = f"Error occur at createCustomerUser: {ex}"
    #     print(f"{datetime.now()} {message}")
    #     return Result(Status=0, Message=message)
