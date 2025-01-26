from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from datetime import datetime
from Core.Models.CollectionEnum import collections
from Utils.GenerateOtp import generateOtp
from Utils.SendOtp import sendOtpOnMobileNumber


def sendOtpMethod(requestBody) -> Result:
    try:
        mongoDb = MongoDBHandler()

        objDict = requestBody.dict()

        otp = generateOtp()

        objDict["OTP"] = otp

        existingBussinessDocument = mongoDb.findDocument(
            collections.BusinessDetails.value, {"PhoneNumber": objDict["PhoneNumber"]}
        )

        existingCustomerDocument = mongoDb.findDocument(
            collections.Customers.value, {"PhoneNumber": objDict["PhoneNumber"]}
        )

        if existingBussinessDocument.Data or existingCustomerDocument.Data:
            return Result(
                Status=400, Message="User is Already Exist with Given Mobile Number"
            )

        existingOtpDocument = mongoDb.findDocument(
            collections.OtpDetails.value, {"PhoneNumber": objDict["PhoneNumber"]}
        )

        if existingOtpDocument.Data:
            # Update the OTP field in the existing document
            mongoDb.update_document(
                collections.OtpDetails.value,
                {"PhoneNumber": objDict["PhoneNumber"]},  # Query to find the document
                {"$set": {"Otp": otp}}  # Update operation to set the new OTP
            )
        else:
            # Insert a new document if it doesn't exist
            mongoDb.insertDocument(collections.OtpDetails.value, objDict)


        sendOtpOnMobileNumber(otp, objDict["PhoneNumber"])

        return Result(Status=200, Message="OTP Sent Successfully")

    except Exception as ex:
        message = f"Error occur at sendOtpMethod: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
