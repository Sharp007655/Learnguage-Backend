from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .constant import *
from .webhook import route
from .models import *
import json

# Create your views here.


# Webhookを受け取り、routeを実行する

@csrf_exempt
def webhook(request):
    
    data = json.loads(request.body.decode('utf-8'))
    
    route(data)
    
    return JsonResponse({ 'message': 'webhook' })
