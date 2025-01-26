from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from datetime import datetime
from Core.Models.CollectionEnum import collections
from Utils.GenerateNumber import generateRandomNumber


def signUpBussinessMember(BussinessUsersRequest) -> Result:
    try:
        mongoDb = MongoDBHandler()

        # Check if the email already exists in the database
        existingMember = mongoDb.findDocument(
            collections.BussinessMember.value, {"Email": BussinessUsersRequest.Email}
        )

        if existingMember.Data:
            return Result(Status=400, Message="User Already Exist")

        # Convert the model to a dictionary and insert it into MongoDB
        memberDict = BussinessUsersRequest.dict(by_alias=True)

        memberDict["_id"] = generateRandomNumber()

        result = mongoDb.insertDocument(collections.BussinessMember.value, memberDict)

        if result.Status == 2:
            signUpBussinessMember(BussinessUsersRequest)

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="Bussiness User Created Succesfully"
        )

    except Exception as ex:
        message = f"Error occur at signUpBussiness: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
