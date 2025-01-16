from fastapi import APIRouter, Depends
from Core.Entities.Bussiness.BusinessDetails import BusinessDetailsModel
from Services.Bussiness.Create.BussinessDetails import signUpBusinessDetails
from Core.Models.ResultModel import Result
from Services.Bussiness.Get.GetAllBusinessDetails import getAllBusinessDetails
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.LocationRequest import LocationRequest
from typing import Optional
from Core.Entities.Bussiness.BusinessDetails import BusinessDetailsUpdateModel
from Services.Bussiness.PatchAPIS.PatchBusinessDetails import updateBusinessDetails
from Services.Bussiness.FilterAPIS.getBussinessDetails import filterBusinessDetails
from Services.Bussiness.Get.GetCompleteBussinessDetails import getBusinessCompleteDetails


BusinessDetails = APIRouter()


# API To Create Bussiness Detail
@BusinessDetails.post("/create/")
def createBusinessDetails(details: BusinessDetailsModel):
    return signUpBusinessDetails(details)


# API to List the All Bussiness Detail
@BusinessDetails.get("/list/")
def listAllBusinessDetails():
    return getAllBusinessDetails()


@BusinessDetails.get("/filter/")
def BussinessDetailFilteration(UserLocation: Optional[LocationRequest]=None,BussinessType: Optional[str] = None,ServiceName : Optional[str]= None,Location : Optional[str]=None,BussinessName: Optional[str]=None):
    return filterBusinessDetails(
        UserLocation, ServiceName, BussinessType, Location, BussinessName
    )

@BusinessDetails.get("/alldetails/{business_id}")
def getCompleteDetails(business_id: int):
    return getBusinessCompleteDetails(business_id)


@BusinessDetails.patch("/update/{business_id}")
def updateBusinessDetailsEndpoint(business_id: int, member: BusinessDetailsUpdateModel):
    return updateBusinessDetails(business_id, member)
