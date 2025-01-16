from fastapi import APIRouter, Depends
from Services.Bussiness.Create.BussinessTeamPresenceDetail import createStaff
from Core.Entities.Bussiness.BussinessStaff import StaffModel
from Core.Entities.Bussiness.BussinessStaff import TeamPresenceUpdateModel
from Services.Bussiness.PatchAPIS.PatchStaff import updateTeamPresence
from Services.Bussiness.Get.GetAllStaff import getAllStaff
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result
from typing import List

Staff = APIRouter()


# API to create Upload staff detail
@Staff.post("/create")
def CreateStaff(
    teamPresence: List[StaffModel]
    # , tokenData: bool = Depends(tokenRequiredCheck)
) -> Result:
    
    # if tokenData is not True:
    #     return Result(Status=401, Message="Token is Not valid")
    return createStaff(teamPresence)


@Staff.get("/list/")
def listAllStaff():
    return getAllStaff()


# API to Update Team Presence 78538803
@Staff.patch("/update/{business_id}")
def updateTeamPresenceEndpoint(business_id: int, member: TeamPresenceUpdateModel):
    return updateTeamPresence(business_id, member)
