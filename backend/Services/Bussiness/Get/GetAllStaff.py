from datetime import datetime
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result
from typing import List


def getAllStaff():
    try:
        mongoDb = MongoDBHandler()

        # Retrieve all business members from the database
        members = mongoDb.findDocuments(collections.TeamPresence.value, {})

        # Convert each document  to a BusinessMemberModel instance and return the list
        return members.Data

    except Exception as ex:
        message = f"Error occur at getAllStaff: {ex}"
        print(f"{datetime.now()} {message}")
        return []
