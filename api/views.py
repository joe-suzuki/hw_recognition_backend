from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .tensorflow import image_preprocessing


@csrf_exempt
def predict(request):
    body = json.loads(request.body)
    base64_string = body["image"].split(",")[1]
    numpy_image = image_preprocessing.base64_to_numpy(base64_string)

    print(body)

    return HttpResponse(status=200)