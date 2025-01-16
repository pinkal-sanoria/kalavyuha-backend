from database.CRUD import MongoDBHandler
from Core.Models.ResultModel import Result
from Core.Models.CollectionEnum import collections
from Core.Entities.Bussiness.BussinessProducts  import ProductInfoModel
from typing import List
from Utils.GenerateNumber import generateRandomNumber
from datetime import datetime


# Add Multiple products
def createProducts(ProductInfoRequest:List[ProductInfoModel]) -> Result:
    try:

        mongoDb = MongoDBHandler()

        # Convert the model to a dictionary and insert it into MongoDB
        productInfoDicts = []
        for product in ProductInfoRequest:
            product_dict = product.dict(by_alias=True)

            product_dict["_id"] = generateRandomNumber()

            # Add discounted price to the dictionary
            if product.isDiscount and product.DiscountPercentage:
                product_dict["DiscountedPrice"] = product.Price * (
                    1 - product.DiscountPercentage / 100
                )
            else:
                product_dict["DiscountedPrice"] = product.Price

            productInfoDicts.append(product_dict)

        result = mongoDb.insertDocuments(
            collections.Products.value, productInfoDicts
        )

        # Return a dictionary with the inserted ID
        return Result(
            Data=result.Data, Status=200, Message="Product is added Successfully"
        )

    except Exception as ex:
        message = f"Error occur at addproductInfo: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Message=message)
