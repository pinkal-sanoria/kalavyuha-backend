from fastapi import APIRouter
from Core.Entities.Bussiness.BussinessProducts  import ProductInfoModel
from Utils.TokenRequired import tokenRequiredCheck
from Core.Models.ResultModel import Result
from typing import List
from Services.Bussiness.Create.BussinessProducts import createProducts
from Services.Bussiness.Get.GetProducts import fetchProducts

Products = APIRouter()


# ApI To Login Customer
@Products.post("/create")
def productCreation(RequestBody: List[ProductInfoModel]) -> Result:
    return createProducts(RequestBody)

@Products.post("/create")
def getProducts(RequestBody: ProductInfoModel) -> Result:
    return fetchProducts(RequestBody)
