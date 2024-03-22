from django.contrib import admin
from .models import UploadImage, EmailCrudData
# Register your models here.

admin.site.register(UploadImage)

class EmailCrudDataAdmin(admin.ModelAdmin):
    list_display = ['title','subject','content','status','slug']
    # exclude = ('slug',)
admin.site.register(EmailCrudData, EmailCrudDataAdmin)