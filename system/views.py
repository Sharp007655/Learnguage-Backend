from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .constant import *
from .webhook import route
from .models import *
from .send import *
import json

# Create your views here.


# Webhookを受け取り、routeを実行する

def healthcheck(request):
    
    return JsonResponse({ 'status': 'running' })


@csrf_exempt
def webhook(request):
    
    data = json.loads(request.body.decode('utf-8'))
    
    route(data)
    
    return JsonResponse({ 'message': 'webhook' })


@csrf_exempt
def userDict(request):
    
    if request.method == GET and FRONT_ID_TOKEN in request.GET:
        
        user = tokenToUser(request.GET[FRONT_ID_TOKEN])
        
        user_words = UserWordData.objects.filter(user=user.id)
        
        words = []
        
        for user_word in user_words:
            
            word = AllWordData.objects.get(id=user_word.word)
            
            dic = { 
                "word": word.word,
                "read": word.read,
                "mean": word.mean,
                "count": user_word.count,
            }
            
            words.append(dic)
        
        return JsonResponse({
            "status": "success",
            "words": words
        })
    
    elif request.method == GET:
        
        words = AllWordData.objects.all()
        
        word_arr = []
        
        for word in words:
            
            dic = { 
                "word": word.word,
                "read": word.read,
                "mean": word.mean,
            }
            
            word_arr.append(dic)
        
        return JsonResponse({
            "status": "success",
            "words": word_arr
        })
    
    else:
        
        return JsonResponse({ "status": "failure" })
