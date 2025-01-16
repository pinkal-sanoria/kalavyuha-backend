from fastapi import HTTPException
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result


def updateBusinessDetails():
    try:
        mongoDb = MongoDBHandler()

        # Prepare update data
        filterQuery = {"BussinessType": "Beauty"}

        # Query MongoDB collection for matching business details
        businessDetails = mongoDb.findDocuments(
            collections.BusinessDetails.value, filterQuery
        )

        if not businessDetails.Data:
            return Result(Status=404, Message="Data Not Found")

        return Result(
            Data=businessDetails.Data,
            Status=200,
            Message="Data Retrived Successfully",
        )

    except Exception as ex:
        print(f"{datetime.now()} Error occurred during business details update: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
