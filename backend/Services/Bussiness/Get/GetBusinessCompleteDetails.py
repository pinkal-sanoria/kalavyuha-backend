from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from database.CRUD import MongoDBHandler
from datetime import datetime
from typing import Dict, Any

def getBusinessCompleteDetails(business_id: int) -> Dict[str, Any]:
    try:
        mongodb = MongoDBHandler()
        
            
        # Get business details
        business_details = mongodb.findDocument(
            collections.BusinessDetails.value,
            {"_id": business_id}
        )
       
        # Get staff details
        staff_details = mongodb.findDocuments(
            collections.TeamPresence.value,
            {"BussinessId": business_id}
        )
       
        # Get services
        services = mongodb.findDocuments(
            collections.ServiceInfo.value,
            {"BussinessId": business_id}
        )
        
        complete_details = {
            # "business_member": business_member.Data,
            "business_details": business_details.Data,
            "staff_details": staff_details.Data if staff_details.Data else [],
            "services": services.Data if services.Data else []
        }
    
        return complete_details
        
    except Exception as ex:
        message = f"Error occurred while getting business complete details: {ex}"
        print(f"{datetime.now()} {message}")
        return {
            "business_member": None,
            "business_details": None,
            "staff_details": None,
            "services": None
        }