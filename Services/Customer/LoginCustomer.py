from Core.Models.ResultModel import Result
from database.CRUD import MongoDBHandler
from Utils.HashPassword import verifyPassword
from datetime import datetime
from Core.Models.CollectionEnum import collections

# Customer Login Request
def loginUser(loginRequestData) -> Result:
    try:
        mongoDb = MongoDBHandler()

        customerCollection = mongoDb.getCollection(collections.Customers.value)

        user = customerCollection.find_one({"PhoneNumber": loginRequestData.PhoneNumber})

        if not user or not verifyPassword(loginRequestData.Password, user["Password"]):
            return Result(Status=0, Message="Invalid Credentials")

        if not user["is_verified"]:
            return Result(Status=400, Message="Account not verified. Please verify OTP.")

        return Result(Status=200, Message="Login Successfully")

    except Exception as ex:
        message = f"Error occur at createCustomerUser: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=400, Message=message)
