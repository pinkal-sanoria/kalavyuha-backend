from fastapi import APIRouter, Depends
from Core.Entities.Customer.FavoriteServiceModel import FavoriteServiceModel
from Services.Bussiness.Create.BussinessFacilities import createFacilities
from Core.Models.ResultModel import Result


Facilities = APIRouter()


# Creat Customer Favorite Service
@Facilities.post("/create/")
def facilitiesCreation(Favorite: FavoriteServiceModel):
    return createFacilities(Favorite)
