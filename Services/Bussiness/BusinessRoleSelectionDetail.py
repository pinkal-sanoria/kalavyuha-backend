from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result

def addBusinessDocuments(BusinessDocuments)->Result:
    try:
        mongoDb = MongoDBHandler()
        
        documentsDict = BusinessDocuments.dict(by_alias = True)
        
        result = mongoDb.insertDocument(collections.Documents.value,documentsDict)

        if result.Status == 2: #if duplication ID is there

            addBusinessDocuments(BusinessDocuments)
        
        return Result(Data=result.Data,Status=200,Message="Documents Created Succesfuly")
    
    except Exception as ex:

        message = f"Error occur at signUpBusinessDetails: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
    

    
    
