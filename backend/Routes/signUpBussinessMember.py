from fastapi import APIRouter, Depends
from Core.Entities.Bussiness.BussinessMember import BusinessMemberModel
from Services.Bussiness.Create.BussinessSignup import signUpBussinessMember
from Core.Entities.Bussiness.BussinessMember import BusinessMemberUpdateModel
from Services.Bussiness.Get.GetBussinessSignup import getAllBusinessMembers
from Services.Bussiness.PatchAPIS.PatchBussinessMember import updateBusinessMember
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result

BusinessMember = APIRouter()


# API to Add New User Member
@BusinessMember.post("/create/")
def createBusinessMember(member: BusinessMemberModel) -> Result:
    return signUpBussinessMember(member)


# API to List All Business Members
@BusinessMember.get("/list/")
def listAllBusinessMembers():
        return getAllBusinessMembers()


@BusinessMember.patch("/update/{business_id}")
def updateBusinessMembers(business_id: int, member: BusinessMemberUpdateModel):
    return updateBusinessMember(business_id, member)
