from fastapi import APIRouter
from Core.Entities.Bussiness.BussinessDocuments import DocumentsDetailsModel
from Services.Bussiness.BusinessRoleSelectionDetail import addBusinessDocuments
from  Services.Bussiness.Get.GetBusinessDocuments import getBusinessDocuments

from typing import List

Documents = APIRouter()

@Documents.post("/create/")
def addDocuments(requestBody: DocumentsDetailsModel):
    return addBusinessDocuments(requestBody)

@Documents.get("/list", response_model=List[DocumentsDetailsModel])
def listBusinessDocuments():
    return getBusinessDocuments()