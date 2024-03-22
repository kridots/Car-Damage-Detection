from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from car_image_detect.models import EmailCrudData
from django.utils.html import strip_tags

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # print(first_name, last_name, username, email, password)
        user_obj = User.objects.filter(email=email)
        user_obj2 = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request,"Your Email already exist")
            return HttpResponseRedirect(request.path_info)
        
        if user_obj2.exists():
            messages.warning(request,"Your Username already exist")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username)
        user_obj.set_password(password)
        user_obj.save()

        # Send WelCome Mail
        data = EmailCrudData.objects.get(slug='welcome-email')
        if data:
            message = strip_tags(data.content)
            body = message.replace("&nbsp;", "<br>").replace('##USER_NAME##', first_name+' '+last_name)
            subject = data.subject
            subject1 = subject.replace('##USER_NAME##', first_name+' '+last_name)
            send_mail(
                    subject=subject1,
                    message=strip_tags(body),
                    from_email='ds27@24livehost.com',  # Update with your email
                    recipient_list=[email],  # Assuming email is provided during registration
                    fail_silently=False,
                )

            return redirect('upload_img')
            
    return render(request, 'auth/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # print(username, password)
        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request,"Account not found!")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=username, password=password)

        if user_obj:
            auth_login(request,user_obj)
            if request.user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('upload_img')
        else:
            messages.warning(request,"Account not found!")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
