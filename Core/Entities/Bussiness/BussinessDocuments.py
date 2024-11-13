from pydantic import BaseModel, Field
from typing import Optional,List
from Utils.GenerateNumber import generateRandomNumber

class DocumentsDetailsModel(BaseModel):
    Id: Optional[int] = Field(default=generateRandomNumber(),alias="_id")
    PanCard: Optional[str] = None
    GstCertification: Optional[str] = None
    BusinessLicense: Optional[str] = None
    InsuranceCertificate: Optional[str] = None
    UtilityBills: Optional[str] = None
    Images: Optional[List[str]] = None
    