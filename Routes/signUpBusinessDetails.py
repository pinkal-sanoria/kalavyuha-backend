from fastapi import APIRouter
from Core.Entities.Bussiness.BusinessDetails import BusinessDetailsModel
from Services.Bussiness.BussinessDetails import signUpBusinessDetails
from Core.Models.ResultModel import Result
from  Services.Bussiness.Get.GetAllBusinessDetails import getAllBusinessDetails
from typing import List

CreateBusinessDetails = APIRouter()

@CreateBusinessDetails.post("/create/")
def createBusinessDetails(details: BusinessDetailsModel)->Result:
    return signUpBusinessDetails(details)

@CreateBusinessDetails.get("/list/", response_model=List[BusinessDetailsModel])
def listAllBusinessDetails():
    return getAllBusinessDetails()





