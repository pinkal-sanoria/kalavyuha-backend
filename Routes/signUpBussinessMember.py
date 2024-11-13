from fastapi import APIRouter
from Core.Entities.Bussiness.BussinessMember import BusinessMemberModel
from Services.Bussiness.BussinessSignup import signUpBussinessMember
from  Services.Bussiness.Get.GetBussinessSignup import getAllBusinessMembers
from typing import List

CreateBusinessMember = APIRouter()

#API to Add New User Member 
@CreateBusinessMember.post("/create/")
def createBusinessMember(member: BusinessMemberModel):
    return signUpBussinessMember(member)

# API to List All Business Members
@CreateBusinessMember.get("/list/", response_model=List[BusinessMemberModel])
def listAllBusinessMembers():
    return getAllBusinessMembers()