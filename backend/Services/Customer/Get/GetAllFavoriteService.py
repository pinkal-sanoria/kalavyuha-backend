from datetime import datetime
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result 
from typing import List

def listAllFavoriteService():

    try:
        mongoDb = MongoDBHandler()
        
        members = mongoDb.findDocuments(collections.FavoriteService.value, {})
        
        return members.Data 
    
    except Exception as ex:
        message = f"Error occur at Favorite Service: {ex}"
        print(f"{datetime.now()} {message}")
        return []
    
    
def FavoriteServiceById(UserId: str):
    try:
        # Initialize MongoDB handler
        mongoDb = MongoDBHandler()

        # Query to find Favorite by UserId
        query = {"UserId": UserId}

        # Fetch Favorite from the database
        Favorite = mongoDb.findDocuments(collections.FavoriteService.value, query)

        # Return the reviews data
        return {
            "Status": 200,
            "Message": "Customer reviews fetched successfully",
            "Data": Favorite
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