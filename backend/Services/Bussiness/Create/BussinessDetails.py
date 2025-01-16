from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result
from Utils.GenerateNumber import generateRandomNumber
from Core.Entities.Bussiness.BusinessDetails import BusinessDetailsModel
from Utils.HandleUploadedFiles import handleUploadToS3
from dotenv import load_dotenv
import os

load_dotenv()

bucketName = os.getenv("BucketName")

def signUpBusinessDetails(BusinessDetailsRequest: BusinessDetailsModel) -> Result:
    try:
        mongoDb = MongoDBHandler()

        # Check if the business name already exists in the database
        existingBusiness = mongoDb.findDocument(
            collections.BusinessDetails.value,
            {"BusinessName": BusinessDetailsRequest.BusinessName},
        )

        # Url = handleUploadToS3(file, bucketName)

        if existingBusiness.Data:
            return Result(Status=400, Message="Business name already exists.")

        # Convert the model to a dictionary and insert it into MongoDB
        businessDict = BusinessDetailsRequest.dict(by_alias=True)

        businessDict["_id"] = generateRandomNumber()

        result = mongoDb.insertDocument(collections.BusinessDetails.value, businessDict)

        if result.Status == 2:
            signUpBusinessDetails(BusinessDetailsRequest)

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="Bussiness Detail Saved Successfully"
        )

    except Exception as ex:
        message = f"Error occur at signUpBusinessDetails: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
