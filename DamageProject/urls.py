"""
URL configuration for DamageProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from car_image_detect.views import upload_image
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('upload/',upload_image, name='upload_img'),
    path('',include('accounts.urls')),
    path('administer/',include('car_image_detect.urls')),
    path('api/',include('api.urls')),
    # # path('administer/',include('CMS.urls')),
    # path('ckeditor/upload', include('ckeditor_uploader.urls')),


    # path('/',include('frented')),
    # path('administer', include('admin')),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    # serving media files only on debug mode
    urlpatterns += [
        path(r'^media/(?P<path>.*)$', static, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
    