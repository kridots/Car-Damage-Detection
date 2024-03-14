from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image_path = models.ImageField(upload_to='car_images/')

    def __str__(self) -> str:
        return str(self.id)