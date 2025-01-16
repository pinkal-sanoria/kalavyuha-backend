from fastapi import APIRouter, Depends
from Services.Bussiness.Create.BussinessServiceDetail import addMultipleServices
from Services.Bussiness.Get.GetDeals import getDailyDeals
from Core.Entities.Bussiness.BussinessService import ServiceInfoModel
from Services.Bussiness.Get.GetAllServices import getAllServices
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result
from typing import List

ServiceInfo = APIRouter()

# Create Multiple Services
@ServiceInfo.post("/create")
# def createServices(
#     serviceInfos: List[ServiceInfoModel], tokenData: bool = Depends(tokenRequiredCheck)
# ) -> Result:
#     if tokenData is not True:
#         return Result(Status=401, Message="Token is Not valid")
#     return addMultipleServices(serviceInfos)
def createServices(
    serviceInfos: List[ServiceInfoModel]):
    return addMultipleServices(serviceInfos)


@ServiceInfo.get("/list/", response_model=List[ServiceInfoModel])
def listAllervices():
    return getAllServices()


@ServiceInfo.get("/deals/")
def getDeals() -> Result:
    return getDailyDeals()