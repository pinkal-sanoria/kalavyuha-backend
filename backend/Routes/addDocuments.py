from fastapi import APIRouter, Depends, UploadFile, File
from Core.Entities.Bussiness.BussinessDocuments import DocumentsDetailsModel
from Services.Bussiness.Create.BusinessDocuments import addBusinessDocuments
from Services.Bussiness.Get.GetBusinessDocuments import getBusinessDocuments
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result
from typing import List, Optional

Documents = APIRouter()

# API to upload Documents
@Documents.post("/create/")
def addDocuments(
    PanCard: Optional[UploadFile] = File(None),
    GstCertification: Optional[UploadFile] = File(None),
    BusinessLicense: Optional[UploadFile] = File(None),
    InsuranceCertificate: Optional[UploadFile] = File(None),
    UtilityBills: Optional[UploadFile] = File(None),
    Images: Optional[List[UploadFile]] = File(None),
    tokenData: bool = Depends(tokenRequiredCheck),
) -> Result:
    files = {
        "PanCard": PanCard,
        "GstCertification": GstCertification,
        "BusinessLicense": BusinessLicense,
        "InsuranceCertificate": InsuranceCertificate,
        "UtilityBills": UtilityBills,
        "Images": Images,
    }

    if tokenData is not True:
        return Result(Status=401, Message="Token is Not valid")

    return addBusinessDocuments(files)


# API to List Document
@Documents.get("/list", response_model=List[DocumentsDetailsModel])
def listBusinessDocuments():
    return getBusinessDocuments()
