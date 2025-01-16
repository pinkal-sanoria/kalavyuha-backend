from datetime import datetime
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result
from typing import List


def getAllBusinessMembers():
    try:
        mongoDb = MongoDBHandler()

        # Retrieve all business members from the database
        members = mongoDb.findDocuments(collections.BussinessMember.value, {})

        # Convert each document (which is a dictionary) to a BusinessMemberModel instance and return the list
        return members.Data  # Ensure member is a dict
    except Exception as ex:
        message = f"Error occur at getAllBusinessMembers: {ex}"
        print(f"{datetime.now()} {message}")
        return []
