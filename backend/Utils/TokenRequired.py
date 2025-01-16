from fastapi import HTTPException, Header
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result
from datetime import datetime


def tokenRequiredCheck(authorization: str = Header(None)):
    try:
        if not authorization or not authorization.startswith("Bearer "):
            print("Not Invalid")
            return False

        # Extract the token
        token = authorization.split("Bearer ")[-1]

        # Verify the token in MongoDB
        mongoDb = MongoDBHandler()

        token_data = mongoDb.findDocument(
            collections.UserCredentails.value, {"Token": token}
        )

        if not token_data:
            print("Token Invalid")
            return False
        # Token is valid; return the token data for further use in the endpoint
        return True

    except Exception as ex:
        message = f"Error occur at tokenRequiredCheck: {ex}"
        print(f"{datetime.now()} {message}")
        return False
