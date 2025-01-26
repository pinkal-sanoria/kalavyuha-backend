from Core.Models.ResultModel import Result
from database.CRUD import MongoDBHandler
from Utils.HashPassword import verifyPassword
from datetime import datetime
from Utils.GenerateRandomString import generateRandomString
from Core.Entities.UserCredentials import UserCredentails
from Core.Models.CollectionEnum import collections


# Customer Login Request
def loginMerchant(loginRequestData) -> Result:
    try:
        mongoDb = MongoDBHandler()

        existingMember = mongoDb.findDocument(
            collections.BussinessMember.value,
            {"PhoneNumber": f"{loginRequestData.PhoneNumber}"},
        )

        if not existingMember.Data or not verifyPassword(
            loginRequestData.Password, existingMember.Data["Password"]
        ):
            return Result(Status=0, Message="Invalid Credentials")

        if not existingMember.Data["IsVerified"]:
            return Result(
                Status=400, Message="Account not verified. Please verify OTP."
            )

        creation_time = datetime.now()

        # expire_time = creation_time + timedelta(minutes=50)

        # Create UserCredentials object with the required fields
        userCredentials = UserCredentails(
            UserId=existingMember.Data.get("_id"),
            UserRole="Merchant",
            Token=generateRandomString(),
            CreationTime=creation_time,
        )

        result = mongoDb.insertDocument(
            collections.UserCredentails.value,
            userCredentials.dict(by_alias=True),
        )

        return Result(Data=result.Data, Status=1, Message="Login Successfully")

    except Exception as ex:
        message = f"Error occur at loginUser: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=400, Message=message)
