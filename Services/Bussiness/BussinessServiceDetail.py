from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from typing import List
from Core.Entities.Bussiness.BussinessService import ServiceInfoModel
from datetime import datetime

def addSingleService(ServiceInfoRequest)->Result:
    try:
        mongoDb = MongoDBHandler()        
        
        # Convert the model to a dictionary and insert it into MongoDB
        serviceInfoDict = ServiceInfoRequest.dict(by_alias=True)

        result = mongoDb.insertDocument(collections.ServiceInfo.value,serviceInfoDict)
                
        # Return a dictionary with the inserted ID
        return Result(Data = result.Data,Status=200, Message="Service is added Successfully")
    
    except Exception as ex:

        message = f"Error occur at addServiceInfo: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
    

# Add Multiple Services 
def addMultipleServices(ServiceInfoRequest:List[ServiceInfoModel])->Result:
    try:
        mongoDb = MongoDBHandler()        
        
        # Convert the model to a dictionary and insert it into MongoDB
        serviceInfoDicts = [service.dict(by_alias=True) for service in ServiceInfoRequest]

        result = mongoDb.insertDocument(collections.ServiceInfo.value,serviceInfoDicts)
                
        # Return a dictionary with the inserted ID
        return Result(Data = result.Data,Status=200, Message="Service is added Successfully")
    
    except Exception as ex:

        message = f"Error occur at addServiceInfo: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)


