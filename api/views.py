from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .tensorflow import image_preprocessing
from .tensorflow import predict_mnist


@csrf_exempt
def predict(request):
    body = json.loads(request.body)
    base64_string = body["image"].split(",")[1]
    numpy_image = image_preprocessing.base64_to_numpy(base64_string)
    predicted_label, prediction_prob = predict_mnist.predict(numpy_image)

    response_body = {
        "predicted_label": str(predicted_label),
        "prediction_prob": prediction_prob
    }

    response_json = json.dumps(response_body, ensure_ascii=False, indent=2)

    return HttpResponse(response_json, status=200)