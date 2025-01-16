from fastapi import APIRouter, Depends
from Core.Models.ResultModel import Result
from Core.Entities.Bussiness.BussinessFacilities import BusinessAmenitiesModel
from Services.Bussiness.Create.BussinessFacilities import createFacilities

BussinessFacilities = APIRouter()


# Create Customer Account
@BussinessFacilities.post("/Location/")
def locatinByPincode(requestBody: BusinessAmenitiesModel) -> Result:
    # if tokenData is not True:
    #     return Result(Status=401, Message="Token is Not valid")
    return createFacilities(requestBody)
