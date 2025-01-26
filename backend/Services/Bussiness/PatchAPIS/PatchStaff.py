from fastapi import HTTPException
from datetime import datetime
from pytz import timezone
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections


def updateTeamPresence(business_id: int, member):
    try:
        mongoDb = MongoDBHandler()

        # Prepare update data
        update_data = {k: v for k, v in member.dict(exclude_unset=True).items()}

        # Add UpdatedOn timestamp
        update_data["UpdatedOn"] = datetime.now(timezone("Asia/Kolkata")).strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )

        # Check if the team record exists
        existing_team = mongoDb.findDocument(
            collections.TeamPresence.value, {"_id": business_id}
        )

        if not existing_team.Data:
            raise HTTPException(status_code=404, detail="Team presence not found")

        # Update the team record
        result = mongoDb.update_document(
            collections.TeamPresence.value, {"_id": business_id}, {"$set": update_data}
        )
        print(result)

        return {"message": "Team presence updated successfully", "data": result}

    except Exception as ex:
        print(f"{datetime.now()} Error occurred during team presence update: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
