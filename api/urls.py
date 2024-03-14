from django.urls import path, include
from .views import pred_img_api

urlpatterns = [
    path("pred-img-api",pred_img_api ,name='pred_img_api'),
  
]