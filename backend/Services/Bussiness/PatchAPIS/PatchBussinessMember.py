from fastapi import APIRouter, HTTPException
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from datetime import datetime
from pytz import timezone


# test id: 35580024
def updateBusinessMember(business_id: int, member):
    try:
        mongoDb = MongoDBHandler()

        # Prepare update data
        update_data = {
            k: v
            for k, v in member.dict(exclude_unset=True).items()
            if k not in ["CreatedOn", "CreatedBy", "BussinessId"]
        }

        # Add UpdatedOn timestamp
        update_data["UpdatedOn"] = datetime.now(timezone("Asia/Kolkata")).strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )

        # Check if the business member exists
        existing_member = mongoDb.findDocument(
            collections.BussinessMember.value, {"_id": business_id}
        )

        if not existing_member.Data:
            raise HTTPException(status_code=404, detail="Business member not found")

        result = mongoDb.update_document(
            collections.BussinessMember.value,
            {"_id": business_id},
            {"$set": update_data},
        )
        print(result)

        return {"message": "Business Member Updated Successfully", "data": result}

    except Exception as ex:
        print(f"{datetime.now()} Error occurred during business member update: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
