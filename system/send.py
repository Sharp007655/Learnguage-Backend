from .constant import *
from .models import *
from . import LINE_Endpoint
import requests, json


# リプライを送信する
# objects: array, reply_token: string

def sendReply(objects, reply_token):
    
    data = { 
        "replyToken": reply_token,
        "messages": objects
    }
    
    data = json.dumps(data)
    
    requests.post(LINE_Endpoint.REPLY, data=data, headers=HEADERS_JSON)



def sendReplyValidate(objects, reply_token):
    
    data = { 
        "replyToken": reply_token,
        "messages": objects
    }
    
    data = json.dumps(data)
    
    response = requests.post(LINE_Endpoint.REPLY_VALIDATE, data=data, headers=HEADERS_JSON)



def sendLoadingAnimation(chat_id, sec=60):
    
    data = {
        "chatId": chat_id,
        "loadingSeconds": sec
    }
    
    data = json.dumps(data)
    
    requests.post(LINE_Endpoint.LOADING, data=data, headers=HEADERS_JSON)



def tokenToUser(token):
    
    data = {
        "id_token": token,
        "client_id": LOGIN_CHANNEL_ID
    }
    
    response = requests.post(LINE_Endpoint.ID_TOKEN_VERIFY, data=data)
    
    user_id = response.json()
    
    return UserData.objects.get(user_id=user_id["sub"])
