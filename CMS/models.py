from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class ContentData(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField()
    status = models.BooleanField(default=False)
    slug = AutoSlugField(unique=True, populate_from='title')

    class Meta:
        verbose_name_plural = "CMS-Data"

    def get_absolute_url(self):
        return reverse('email-templets-view', kwargs={'slug': self.slug})
    

    def __str__(self) -> str:
        return str(self.title)