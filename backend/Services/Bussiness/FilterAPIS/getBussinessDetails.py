from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from Core.Models.ResultModel import Result
from Utils.CalculateDistance import calculateDistance
from typing import Optional


def filterBusinessDetails(
    userLocation = None ,
    serviceName: Optional[str] = None,
    businessType: Optional[str] = None,  # Fixed typo in parameter name
    location: Optional[str] = None,
    bussinessName:Optional[str] = None,
) -> Result:
    try:
        mongodb = MongoDBHandler()
        
        business_filter = {}

        if bussinessName:
            business_filter["BusinessName"] = {
                "$regex": r"\b" + bussinessName + r"\b",
                "$options": "i",
            }

        # Build business filter first to minimize database queries
        if businessType:
            business_filter["BussinessType"] = {"$regex": businessType, "$options": "i"}

        if location:
            # Search within the CityState field where the location is part of any word in the CityState
            business_filter["CityState"] = {"$regex": r"\b" + location + r"\b", "$options": "i"}

        # Only query services if serviceName is provided
        if serviceName:
            # Use projection to fetch only BusinessId field
            service_result = mongodb.findDocuments(
                collections.ServiceInfo.value,
                {"ServiceName": serviceName}
            )

            if not service_result.Data:
                return Result(
                    Data=[],
                    Status=200,
                    Message="No businesses found matching the criteria",
                )

            # Extract business IDs and add to filter
            business_ids = [service["BussinessId"] for service in service_result.Data]
            business_filter["_id"] = {"$in": business_ids}

        # Fetch businesses with the combined filter
        business_result = mongodb.findDocuments(
            collections.BusinessDetails.value, business_filter
        )

        businessIds = [service["_id"] for service in business_result.Data]

        complete_details = []

        for business_id in businessIds:
            # Get business details
            business_details = mongodb.findDocument(
                collections.BusinessDetails.value, {"_id": business_id}
            )
            # Get services
            services = mongodb.findDocuments(
                collections.ServiceInfo.value, {"BussinessId": business_id}
            )

            details = {
                "business_details": business_details.Data,
                "services": services.Data if services.Data else [],
            }

            if userLocation:
                # If userlocation is provided, calculate the distance
                user_lat = userLocation.get("Latitude")
                user_lon = userLocation.get("Longitude")

                # Assuming business_details contains latitude and longitude fields
                business_lat = business_details.Data.get("Latitude")
                business_lon = business_details.Data.get("Longitude")

                # Calculate distance using Haversine formula (or your preferred method)
                distance = calculateDistance(
                    business_lat, business_lon, user_lat, user_lon
                )

                # Add the distance to the complete details
                details["distance"] = f"{round(distance, 2)} km"

            # details.sort(
            #     key=lambda x: x.get("distance", float("inf"))
            # )  # Sort by distance, handle missing distance

            complete_details.append(details)

        return Result(
            Data=complete_details, Status=200, Message="Data Retrieved Successfully"
        )

    except Exception as ex:
        message = f"Error occurred in filterBusinessDetails: {ex}"
        print(f"{datetime.now()} - {message}")
        return Result(Status=0, Message=message)