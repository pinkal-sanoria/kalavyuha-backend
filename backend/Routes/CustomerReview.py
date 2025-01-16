from fastapi import APIRouter,Depends
from Core.Entities.Customer.CustomerReview import ReviewsModel
from Services.Customer.CustomerReview import creatCustomerReview
from Services.Customer.Get.GetAllCustomerReview import listAllCustomerReview
from Services.Customer.Get.GetAllCustomerReview import customerReviewById
from Core.Models.ResultModel import Result

CustomerReview = APIRouter()

# Creat Customer Review
@CustomerReview.post("/create/")
def customerReview(review: ReviewsModel): 
    return creatCustomerReview(review)


@CustomerReview.get("/list/")
def customerReview():
    return listAllCustomerReview()


@CustomerReview.get("/list/{UserId}")
def GetcustomerReview(UserId: str):
    return customerReviewById(UserId)