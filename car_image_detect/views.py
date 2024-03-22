from django.shortcuts import render, redirect, HttpResponse
from .models import UploadImage, EmailCrudData
from CMS.models import ContentData
from .forms import UploadImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import is_superuser
from django.contrib.auth.decorators import user_passes_test
# from ...custome import CarDamageDetector
# from custome import CarDamageDetector

import cv2
import os
import sys

# Add the parent directory of custom.py to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Create your views here.


# def predict_image_check(image_path):
#     # Load the model
#     detector = CarDamageDetector()

#     # Load your test image (replace with your image loading logic)
#     # image = cv2.imread("F:\Kritesh\car-damage\dataset\img\\4.jpg")
#     # image = cv2.imread("F:\Kritesh\car-damage\dataset\\val\\3.jpg")
#     image = cv2.imread(image_path)
#     # image = cv2.imread("dataset/test/60.jpg")

#     # Make prediction
#     results = detector.predict(image)
    
#     # Access detections and predicted image
#     detections = results["detections"]
#     predicted_image = results["predicted_image"]

#     # Optional: Process detections or visualize the predicted image
#     # ...
#     # print(predicted_image)
#     # cv2.imshow("Car Damage Detection", predicted_image)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()

#     # Convert the predicted image from OpenCV format to bytes
#     _, buffer = cv2.imencode('.jpg', predicted_image)
#     predicted_image_bytes = buffer.tobytes()

#     return predicted_image_bytes


@login_required(login_url="/login/")
def upload_image(request):
    try:
        if request.method == 'POST':  
            form = UploadImageForm(request.POST, request.FILES)  
            if form.is_valid():  
                up = form.save()  

                # # img_object = form.cleaned_data.get('image_path')
                # img_object = request.FILES['image_path']
                # # imagepath = f'media/car_images/{img_object}'
                # print(img_object)
                # print(up.image_path.path)
                # predicted_image_bytes  = predict_image_check(up.image_path.path)                
                # # return render(request, 'index.html', {'form': form, 'img_obj': up})
                # # Return the predicted image as an HTTP response
                # return HttpResponse(predicted_image_bytes, content_type="image/jpeg")
                # return render(request, 'index.html', {'form': form, 'img_obj': predicted_image_bytes})
                
        else:  
            form = UploadImageForm()  
    except Exception as e:
        print("ERROR:>",e)
    return render(request, 'index.html', {'form': form})


@login_required(login_url="/login/")
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

#------------------------------------------------------------------------------------------
#-----------------------------------Email-Temp---------------------------------------------
#------------------------------------------------------------------------------------------

@login_required(login_url="/login/")
def emailtemp(request):
    if request.method == 'POST':
        title = request.POST['title-data']
        subject = request.POST['subject-data']
        message = request.POST['message-data']
        # status = request.POST.get('status-data')
          # Check if the checkbox is checked
        status = request.POST.get('status-data', False)
        if status == 'on':
            status = True
        else:
            status = False

        # print("title:",title,"subject:",subject,"message:",message,"status:",status)
        userData = EmailCrudData.objects.create(title=title,subject=subject,content=message,status=status)

        if userData:
            userData.save()
            messages.success(request,"Template Save")
            return redirect('email-templets')
        else:
            messages.error(request,"Something went wrong")
            return redirect('email-templetes')
    return render(request,'admin-page/emailTemplate/email_template.html')


@login_required(login_url="/login/")
def emailtemplist(request):
    userData = EmailCrudData.objects.all()
    return render(request,'admin-page/emailTemplate/email_template_list.html',{'data' : userData})


@login_required(login_url="/login/")
def emailtempview(request, slug):
    EmailData = EmailCrudData.objects.get(slug=slug)

    return render(request,'admin-page/emailTemplate/email_template_view.html',{'data' : EmailData})


@login_required(login_url='/login/')
def emailtempedit(request, slug):
    editData = EmailCrudData.objects.get(slug=slug)
    if request.method == 'POST':
        editData.title = request.POST.get('title-data')
        editData.subject = request.POST.get('subject-data')
        editData.content = request.POST.get('message-data')
        editData.status = bool(request.POST.get('status-data'))
        editData.save()
        return redirect('email-templets')
    return render(request,'admin-page/emailTemplate/email_template_edit.html',{'data' : editData})




#---------------------------------------------------------------------------------------------------
#--------------------------------------------CMS-Manger---------------------------------------------
#---------------------------------------------------------------------------------------------------

class ContentManager:
    def contentcreate(request):
        if request.method == 'POST':
            title = request.POST['title-content']
            desciption = request.POST['para-content']
            status = request.POST.get('status-data', False)
            if status == 'on':
                status = True
            else:
                status = False

            usercontentData = ContentData.objects.create(title=title,description=desciption,status=status)
            usercontentData.save()

        return render(request,'cms-page/content-create.html')
    
    @login_required(login_url="/login/")
    def contentlist(request):
        userData = ContentData.objects.all()
        return render(request,'cms-page/content-list.html',{'data': userData})
    
    
    @login_required(login_url="/login/")
    def contentview(request, slug):
        contentData = ContentData.objects.get(slug=slug)

        return render(request,'cms-page/content-view.html',{'data' : contentData})


    @login_required(login_url='/login/')
    def contentedit(request, slug):
        editData = ContentData.objects.get(slug=slug)
        if request.method == 'POST':
            editData.title = request.POST.get('title-data')
            editData.description = request.POST.get('message-data')
            editData.status = bool(request.POST.get('status-data'))
            print(editData)
            editData.save()
            return redirect('content-list')
        return render(request,'cms-page/content-edit.html',{'data' : editData})