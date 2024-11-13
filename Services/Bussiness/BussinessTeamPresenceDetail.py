from database.CRUD import MongoDBHandler
from fastapi import HTTPException
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from datetime import datetime


def createStaff(TeamPresenceRequest)->Result:
    try:
        mongoDb = MongoDBHandler()

        teamPresenceDict = TeamPresenceRequest.dict(by_alias=True)
        result = mongoDb.insertDocument(collections.BussinessMember.value,teamPresenceDict)
        print(result)
      
        return Result(Data=result.Data,Status=200,Message="Bussiness User Created Succesfully")
    
    except Exception as ex:

        message = f"Error occur at signUpBussiness: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
