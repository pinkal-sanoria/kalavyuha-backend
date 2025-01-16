from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from database.CRUD import MongoDBHandler
from datetime import datetime
from typing import Dict, Any


def getBusinessCompleteDetails(business_id: int) -> Result:
    try:
        mongodb = MongoDBHandler()

        # Get business details
        business_details = mongodb.findDocument(
            collections.BusinessDetails.value, {"_id": business_id}
        )

        # Get staff details
        staff_details = mongodb.findDocuments(
            collections.TeamPresence.value, {"BussinessId": business_id}
        )

        # Get services
        services = mongodb.findDocuments(
            collections.ServiceInfo.value, {"BussinessId": business_id}
        )

        bussinessImages = mongodb.findDocument(
            collections.Documents.value, 
            {"BussinessId": business_id},
            {"Images": 1} 
        )

        bussinessFacilities = mongodb.findDocument(
            collections.Facilities.value, {"BussinessId": business_id}
        )

        businessProducts = mongodb.findDocuments(
            collections.Products.value, {"_id": business_id}
        )

        complete_details = {
            "BusinessInfo": business_details.Data,
            "Staffs": staff_details.Data if staff_details.Data else [],
            "Services": services.Data if services.Data else [],
            "BussinessImages": bussinessImages.Data,
            "BussinessProducts": businessProducts.Data if businessProducts.Data else [],
            "bussinessFacilities": bussinessFacilities
        }

        return Result(Data=complete_details,Status=200,Message="Data Retrieved succesfully")

    except Exception as ex:
        message = f"Error occurred while getting business complete details: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(
            Status=400, Message=f"An error Occurred at getBusinessCompleteDetails :{ex} "
        )
