from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result

def signUpBusinessDetails(BusinessDetailsRequest)->Result:
    try:
        mongoDb = MongoDBHandler()
        
        # Check if the business name already exists in the database
        existingBusiness = mongoDb.findDocument(collections.BusinessDetails.value,{"BusinessName": BusinessDetailsRequest.BusinessName})
        
        if existingBusiness.Data:
            return Result(Status=400, Message="Business name already exists.")
        
        # Convert the model to a dictionary and insert it into MongoDB
        businessDict = BusinessDetailsRequest.dict(by_alias= True)

        result = mongoDb.insertDocument(collections.BusinessDetails.value,businessDict)
        
        # Return a dictionary with the inserted ID
        return Result(Data=result.Data,Status=200,Message="Bussiness Detail Saved Successfully")
    
    except Exception as ex:

        message = f"Error occur at signUpBusinessDetails: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)

