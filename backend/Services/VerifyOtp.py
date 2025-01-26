from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from datetime import datetime
from Core.Models.CollectionEnum import collections


def otpVerification(otp: int, phoneNumber: str) -> Result:
    try:
        mongoDb = MongoDBHandler()

        user = mongoDb.findDocument(
            collections.OtpDetails.value, {"PhoneNumber": phoneNumber}
        )

        if not user.Data:
            message = "User not Found with Associated Contact No"
            return Result(Status=404, Message=message)

        if user.Data["OTP"] == otp:
            message = "OTP Verified Successfully"
            return Result(Status=200, Message=message)

        else:
            message = "Invalid OTP ,please Check it again"
            return Result(Status=401, Message=message)

    except Exception as ex:
        message = f"Error occur at otpVerification: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
