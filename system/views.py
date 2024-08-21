from django.http import JsonResponse

# Create your views here.
def webhook(response):
    
    return JsonResponse({ 'message': 'webhook' })
