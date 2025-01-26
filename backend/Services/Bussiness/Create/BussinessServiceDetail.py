from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from typing import List
from Utils.GenerateNumber import generateRandomNumber
from Core.Entities.Bussiness.BussinessService import ServiceInfoModel
from datetime import datetime


# Add Multiple Services
def addMultipleServices(ServiceInfoRequest: List[ServiceInfoModel]) -> Result:
    try:
        mongoDb = MongoDBHandler()

        # Convert the model to a dictionary and insert it into MongoDB
        serviceInfoDicts = []
        for service in ServiceInfoRequest:
            service_dict = service.dict(by_alias=True)

            service_dict["_id"] = generateRandomNumber()

            # Add discounted price to the dictionary
            if service.isDiscount and service.DiscountPercentage:
                service_dict["DiscountedPrice"] = service.Price * (
                    1 - service.DiscountPercentage / 100
                )
            else:
                service_dict["DiscountedPrice"] = service.Price

            serviceInfoDicts.append(service_dict)

        result = mongoDb.insertDocuments(
            collections.ServiceInfo.value, serviceInfoDicts
        )

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="Service is added Successfully"
        )

    except Exception as ex:
        message = f"Error occur at addServiceInfo: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
