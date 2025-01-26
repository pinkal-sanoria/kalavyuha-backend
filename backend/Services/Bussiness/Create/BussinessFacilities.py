from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from Core.Entities.Bussiness.BussinessFacilities import BusinessAmenitiesModel
from typing import List
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime


# Add Multiple facilities
def createFacilities(facilitiesInfoRequest: BusinessAmenitiesModel) -> Result:
    try:
        mongoDb = MongoDBHandler()
        
        facilities_dict = facilitiesInfoRequest.dict(by_alias=True)

        facilities_dict["_id"] = generateRandomNumber()

        result = mongoDb.insertDocument(collections.Facilities.value, facilities_dict)

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="facilities is added Successfully"
        )

    except Exception as ex:
        message = f"Error occur at addfacilitiesInfo: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
