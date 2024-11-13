from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from datetime import datetime
from Core.Models.CollectionEnum import collections

def otpVerification(otp:int,userId:int)->Result: 
    try:
        mongoDb = MongoDBHandler()
        customerCollection = mongoDb.getCollection(collections.BussinessMember.value)

        user = customerCollection.find_one({"_id": userId})
        
        if not user:
            message = "User not Found with Associated Contact No"
            return Result(Status=404, Message=message)
        
        if user['Otp'] == otp:
            mongoDb.update_document(collections.BussinessMember.value,{"_id": userId}, {"$set": {"isVerified": True}})
            message = "OTP Verified Successfully"
            return Result(Status=200, Message=message)
        
        else:
            message = "Invalid OTP ,please Check it again"
            return Result(Status=401, Message=message)
    
    except Exception as ex:
        message = f"Error occur at createCustomerUser: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)