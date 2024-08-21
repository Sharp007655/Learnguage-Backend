from .constant import *
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
    
    requests.post(LINE_Endpoint.REPLY, data=data, headers=HEADERS)
