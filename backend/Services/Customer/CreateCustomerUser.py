from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Utils.HashPassword import hashPassword
from datetime import datetime
from Core.Models.CollectionEnum import collections


# Create Customer Record
def createNewCustomerAccount(customerObj) -> Result:
    try:
        mongoDb = MongoDBHandler()

        # Check if the email already exists in the database
        existingMember = mongoDb.findDocument(
            collections.Customers.value, {"PhoneNumber": customerObj.PhoneNumber}
        )

        if existingMember.Data:
            return Result(Status=400, Message="User Already Exist")

        # Convert the model to a dictionary and insert it into MongoDB
        memberDict = customerObj.dict(by_alias=True)

        memberDict["Password"] = hashPassword(customerObj.Password)

        result = mongoDb.insertDocument(collections.Customers.value, memberDict)

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="Bussiness User Created Succesfully"
        )

    except Exception as ex:
        message = f"Error occur at createNewCustomerAccount: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
