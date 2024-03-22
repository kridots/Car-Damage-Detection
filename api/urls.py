from django.urls import path, include
from .views import pred_img_api, content_data_update

urlpatterns = [
    path("pred-img-api",pred_img_api ,name='pred_img_api'),
    path("content_data_update",content_data_update ,name='content_data_update'),
  
]