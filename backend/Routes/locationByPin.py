from fastapi import APIRouter, Depends
from Utils.LocationByPostalCode import getLocationByPincode
from Core.Models.ResultModel import Result
from Core.Entities.PinCodeModel import PinCodeModel

PincodeLocation = APIRouter()


# Create Customer Account
@PincodeLocation.post("/Location/")
def locatinByPincode(requestBody: PinCodeModel) -> Result:
    # if tokenData is not True:
    #     return Result(Status=401, Message="Token is Not valid")
    return getLocationByPincode(requestBody)
