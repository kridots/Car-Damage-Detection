from django.shortcuts import render, redirect, HttpResponse
from .models import UploadImage
from .forms import UploadImageForm
from django.contrib.auth.decorators import login_required
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


@login_required(login_url="/accounts/login/")
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