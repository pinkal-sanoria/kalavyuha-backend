from datetime import datetime
from database.CRUD import MongoDBHandler
from Core.Models.CollectionEnum import collections
from Core.Models.ResultModel import Result


def fetchProducts() -> Result:
    try:
        mongoDb = MongoDBHandler()

        products = mongoDb.findDocuments(
            collections.Products.value
        )


        if not products.Data:
            return Result(
                Data=products.Data, Status=404, Messages="No Data is Available"
            )

        return Result(
            Data=products.Data, Status=200, Message="Data Retrived Successfully"
        )

    except Exception as ex:
        message = f"Error occur at getDailyDeals: {ex}"
        print(f"{datetime.now()} {message}")
        return Result(Status=0, Messages=message)
