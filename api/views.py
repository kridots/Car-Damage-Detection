from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .custome import CarDamageDetector
from CMS.models import ContentData

from car_image_detect.models import UploadImage
from car_image_detect.forms import UploadImageForm
from .serializer import UploadImageSerializer
import cv2
import base64

# Create your views here.
@api_view(['POST'])
def pred_img_api(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            up = form.save()  

            img_object = request.FILES['image_path']
        
            print(img_object)
            print(up.image_path.path)
            predicted_image_base64  = predict_image_check(up.image_path.path)                
            # predicted_image_base64 = base64.b64encode(predicted_image_bytes).decode('utf-8')
            return Response(data={'predicted_image':predicted_image_base64[0], "Detact-Result": predicted_image_base64[1]})


def predict_image_check(image_path):
    # Load the model
    detector = CarDamageDetector()

    # Load your test image (replace with your image loading logic)
    # image = cv2.imread("F:\Kritesh\car-damage\dataset\\val\\3.jpg")
    image = cv2.imread(image_path)
    # image = cv2.imread("dataset/test/60.jpg")

    # Make prediction
    results = detector.predict(image)
    
    # Access detections and predicted image
    detections = results["detections"]
    predicted_image = results["predicted_image"]

    # Optional: Process detections or visualize the predicted image
    # ...
    # print(predicted_image)
    # cv2.imshow("Car Damage Detection", predicted_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Convert the predicted image from OpenCV format to bytes
    # predicted_image_bytes = buffer.tobytes()

    # Condition for Detacted marks exist or not
    find_damage = 'Damage' if len(detections['instances'].pred_masks) > 0 else 'Not-Damage'
    # find_damage = True if len(detections['instances'].pred_masks) > 0 else False

    # Convert the predicted image from OpenCV format to base64
    _, buffer = cv2.imencode('.jpg', predicted_image)
    predicted_image_base64 = base64.b64encode(buffer).decode('utf-8')

    # Saving an predicted image on media folder
    cv2.imwrite(image_path, predicted_image)
    return predicted_image_base64, find_damage

@api_view(['POST'])
def content_data_update(request):
    if request.method == 'POST':
        
        try:
            content_data_id = request.POST.get('id')
            new_status = request.POST.get('status')
        except (ValueError, TypeError):
            return JsonResponse({'error': "Invalid data format"}, status=400)
        
        content_data = get_object_or_404(ContentData, pk=content_data_id)
        content_data.status = bool(int(new_status))
        content_data.save()
        return JsonResponse({'success': 'Successfully update status'}, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)