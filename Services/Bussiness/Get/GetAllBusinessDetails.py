from datetime import datetime
import logging
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result
from Core.Entities.Bussiness.BusinessDetails import BusinessDetailsModel


def getAllBusinessDetails():
    try:
        mongoDb = MongoDBHandler()
        
        # Find business details by name
        business = mongoDb.findDocuments(collections.BusinessDetails.value, {})
        
        return business.Data
    except Exception as ex:
        message = f"Error occurred at getBusinessDetails: {ex}"
        print(f"{datetime.now()} {message}")
        return []
