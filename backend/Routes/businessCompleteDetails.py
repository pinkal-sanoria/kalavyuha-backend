from fastapi import APIRouter, Depends, HTTPException
from Core.Models.ResultModel import Result
from Core.Entities.Bussiness.BusinessCompleteDetails import BusinessCompleteDetailsResponse
from Services.Bussiness.Get.GetBusinessCompleteDetails import getBusinessCompleteDetails
from Utils.TokenRequired import tokenRequiredCheck
from typing import List

BusinessCompleteDetailsRouter = APIRouter()
#id 15586055

@BusinessCompleteDetailsRouter.get("/{business_id}")
def get_business_complete_details(business_id: int):
    return getBusinessCompleteDetails(business_id)
    