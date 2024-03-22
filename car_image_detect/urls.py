from django.urls import path, include
from .views import ContentManager,dashboard, emailtemp, emailtemplist, emailtempview, emailtempedit

urlpatterns = [
    # path('',upload_image, name='upload_img'),
    path('dashboard/',dashboard, name='dashboard'),

#----------------------------Email-Temp---------------------------------------
    path('email-templets/list',emailtemplist,name='email-templets'),
    path('email-templets/add',emailtemp,name='email-templets-add'),
    path('email-templets/view/<slug>',emailtempview,name='email-templets-view'),
    path('email-templets/edit/<slug>',emailtempedit,name='email-templets-edit'),
#-------------------------------CMS---------------------------------------------
    path('cms/create/',ContentManager.contentcreate,name='content-create'),
    path('cms/list/',ContentManager.contentlist,name='content-list'),
    path('cms/view/,<slug>',ContentManager.contentview,name='content-view'),
    path('cms/edit/<slug>',ContentManager.contentedit,name='content-edit'),
]



