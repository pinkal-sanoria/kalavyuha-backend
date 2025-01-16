from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime


def createStaff(TeamPresenceRequest) -> Result:
    try:

        mongoDb = MongoDBHandler()
        
        teamPresenceDict = [
            {**TeamMember.dict(by_alias=True), "_id": generateRandomNumber()} 
            for TeamMember in TeamPresenceRequest
        ]

        result = mongoDb.insertDocuments(
            collections.TeamPresence.value, teamPresenceDict
        )
        print(result)

        return Result(
            Data=result.Data, Status=200, Message="Bussiness User Created Succesfully"
        )

    except Exception as ex:
        message = f"Error occur at signUpBussiness: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
