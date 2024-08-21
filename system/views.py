from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .constant import *
from .models import *
from . import endpoint
import json

# Create your views here.
@csrf_exempt
def webhook(request):
    
    data = json.loads(request.body.decode('utf-8'))
    
    if request.method == POST:
        
        print(data['events'][0]['source']['userId'], data['events'][0]['message']['text'])
    
    return JsonResponse({ 'message': 'webhook' })
