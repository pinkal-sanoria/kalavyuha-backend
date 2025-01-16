from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result
from Utils.GenerateNumber import generateRandomNumber
from Core.Entities.Bussiness.BussinessDocuments import DocumentsDetailsModel
from Utils.HandleUploadedFiles import handleUploadToS3
from dotenv import load_dotenv
import uuid
import os

load_dotenv()

bucketName = os.getenv("BucketName")


def addBusinessDocuments(files) -> Result:
    try:
        s3_urls = {}

        for key, file in files.items():
            if file:
                # file_key = f"{uuid.uuid4().hex}_{file.filename}"
                s3_urls[key] = handleUploadToS3(file, bucketName)

        documentRequestBody = DocumentsDetailsModel(**s3_urls)

        print(documentRequestBody, "jcvjfb")

        mongoDb = MongoDBHandler()

        documentsDict = documentRequestBody.dict(by_alias=True)

        documentsDict["_id"] = generateRandomNumber()

        result = mongoDb.insertDocument(collections.Documents.value, documentsDict)

        if result.Status == 2:  # if duplication ID is there
            addBusinessDocuments(files)

        return Result(
            Data="result.Data", Status=200, Message="Documents Created Succesfuly"
        )

    except Exception as ex:
        message = f"Error occur at signUpBusinessDetails: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
