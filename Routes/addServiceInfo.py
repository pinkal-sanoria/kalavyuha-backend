from fastapi import APIRouter
from Services.Bussiness.BussinessServiceDetail import addSingleService,addMultipleServices
from Core.Entities.Bussiness.BussinessService import ServiceInfoModel 
from Services.Bussiness.Get.GetAllServices import getAllServices

from typing import List

CreateServiceInfo = APIRouter()

# Create Service
@CreateServiceInfo.post("/create/")
def createService(serviceInfo: ServiceInfoModel):
    return addSingleService(serviceInfo)

# Create Multiple Services
@CreateServiceInfo.post("/create")
def createServices(serviceInfos : List[ServiceInfoModel]):
    return addMultipleServices(serviceInfos)

@CreateServiceInfo.get("/list/", response_model=List[ServiceInfoModel])
def listAllervices():
    return getAllServices()
