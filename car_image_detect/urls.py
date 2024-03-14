from django.urls import path, include
from .views import upload_image

urlpatterns = [
    path('',upload_image, name='upload_img'),
    # path('upload/',upload_image, name='upload_img'),
]