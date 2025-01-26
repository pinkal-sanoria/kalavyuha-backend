from fastapi import APIRouter,Depends
from Core.Entities.Customer.FavoriteServiceModel import FavoriteServiceModel
from Services.Customer.creatFavoriteService import creatFavoriteService
from Services.Customer.Get.GetAllFavoriteService import listAllFavoriteService
from Services.Customer.Get.GetAllFavoriteService import FavoriteServiceById
from Core.Models.ResultModel import Result


FavoriteService = APIRouter()

# Creat Customer Favorite Service
@FavoriteService.post("/create/")
def favoriteService(Favorite: FavoriteServiceModel): 
    return creatFavoriteService(Favorite)

@FavoriteService.get("/list/")
def getFavoriteServices():
    return listAllFavoriteService()

@FavoriteService.get("/list/{UserId}")
def getFavoriteService(UserId: str):
    return FavoriteServiceById(UserId)