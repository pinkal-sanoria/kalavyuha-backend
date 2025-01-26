from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime
from Core.Entities.Customer.CustomerReview import ReviewsModel
from typing import List

# Mistake in CRUD operation insertDocuments function can't returning data

def creatCustomerReview(review):
    try:
        print(review)

        mongoDb = MongoDBHandler()

        dataDict = review.dict(by_alias=True)

        dataDict["_id"] = generateRandomNumber()
        # result = mongoDb.insertDocument(collections[ReviewsModel])
        # Return a dictionary with the inserted ID
        result = mongoDb.insertDocument(collections.CustomerReview.value, dataDict)

        # Return a success response
        return Result(Data = result.Data, Status=200, Message="User Review Created Successfully")
        
    except Exception as ex:

        message = f"Error occur at User Review: {ex}"
        print(f"{datetime.now()} {message}")
        return []
