from datetime import datetime
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result 
from typing import List

def listAllCustomerReview():

    try:
        mongoDb = MongoDBHandler()
        
        members = mongoDb.findDocuments(collections.CustomerReview.value, {})
        
        return members.Data 
    
    except Exception as ex:
        message = f"Error occur at Customer Review: {ex}"
        print(f"{datetime.now()} {message}")
        return []
    
    
def customerReviewById(UserId: str):
    try:
        # Initialize MongoDB handler
        mongoDb = MongoDBHandler()

        # Query to find reviews by UserId
        query = {"UserId": UserId}

        # Fetch reviews from the database
        reviews = mongoDb.findDocuments(collections.CustomerReview.value, query)

        # Return the reviews data
        return {
            "Status": 200,
            "Message": "Customer reviews fetched successfully",
            "Data": reviews
        }

    except Exception as ex:
        # Log and return the error message
        message = f"Error occurred at Customer Review: {str(ex)}"
        print(f"{datetime.now()} {message}")
        return {
            "Status": 500,
            "Message": message,
            "Data": []
        }