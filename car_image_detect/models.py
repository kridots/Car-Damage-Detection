from django.db import models
# from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class UploadImage(models.Model):
    image_path = models.ImageField(upload_to='car_images/')

    def __str__(self) -> str:
        return str(self.id)
    

class EmailCrudData(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    content = RichTextUploadingField()
    # content = models.TextField()
    status = models.BooleanField(default=False)
    slug = AutoSlugField(unique=True, populate_from='title')
    # slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('email-templets-view', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.slug