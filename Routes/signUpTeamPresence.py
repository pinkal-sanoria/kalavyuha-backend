from fastapi import APIRouter
from Services.Bussiness.BussinessTeamPresenceDetail import createStaff
from Core.Entities.Bussiness.BussinessStaff import TeamPresenceModel
from typing import List
from  Services.Bussiness.Get.GetAllStaff import getAllStaff



Staff = APIRouter()

@Staff.post("/create/")
def CreateStaff(teamPresence: TeamPresenceModel):
    return createStaff(teamPresence)

@Staff.get("/list/", response_model=List[TeamPresenceModel])
def listAllStaff():
    return getAllStaff()