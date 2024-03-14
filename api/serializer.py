from rest_framework import serializers
from car_image_detect.models import UploadImage

class UploadImageSerializer(serializers.Serializer):
    class Meta:
        model = UploadImage
        fields = '__all__' 
