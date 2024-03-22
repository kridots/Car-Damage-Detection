# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# # from ckeditor_uploader import views as ckeditor_views
# from .models import ContentData
# Create your views here.

# @login_required(login_url='/login/')

# class ContentManager:
#     def contentcreate(request):
#         if request.method == 'POST':
#             title = request.POST['title-content']
#             desciption = request.POST['para-content']
#             status = request.POST.get('status-data', False)
#             if status == 'on':
#                 status = True
#             else:
#                 status = False

#             usercontentData = ContentData.objects.create(title=title,description=desciption,status=status)
#             usercontentData.save()

#         return render(request,'cms-page/content-create.html')
    
#     @login_required(login_url="/login/")
#     def contentlist(request):
#         userData = ContentData.objects.all()
#         return render(request,'cms-page/content-list.html',{'data': userData})
    
    
#     @login_required(login_url="/login/")
#     def contentview(request, slug):
#         contentData = ContentData.objects.get(slug=slug)

#         return render(request,'cms-page/content-view.html',{'data' : contentData})


#     @login_required(login_url='/login/')
#     def contentedit(request, slug):
#         editData = ContentData.objects.get(slug=slug)
#         if request.method == 'POST':
#             editData.title = request.POST.get('title-data')
#             editData.description = request.POST.get('message-data')
#             editData.status = bool(request.POST.get('status-data'))
#             print(editData)
#             editData.save()
#             return redirect('content-list')
#         return render(request,'cms-page/content-edit.html',{'data' : editData})