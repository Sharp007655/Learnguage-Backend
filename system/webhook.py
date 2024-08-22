from .constant import *
from .models import *
from .messageFormat import *
from .send import *
from .quiz import *


# リッチメニュー操作時のルートをする関数（未実装）
# user_id: string, message: string, reply_token: string

#def textCommand(user_id, message, reply_token):
    
#    if message == MESSAGE_CHAT_START:
        
#    elif message == MESSAGE_CHAT_FINISH:
        
#    elif message == MESSAGE_QUIZ:
        
#        messages = [ messageTextFormat(RESPONSE_QUIZ) ]
        
#        sendReply(messages, reply_token)
        
#        question = quiz_create(user_id)
        
#    elif message == MESSAGE_ANALYZE:
    


# テキスト入力時のルートをする関数
# 　LLM使用部未実装
# 　モードが違う場合、モード変更を促すメッセージを送信
# user_id: string, message: string, reply_token: string

def textMessage(user_id, message, reply_token):
    
    user = UserData.objects.get(user_id=user_id)
    
    if user.mode == ModeData.objects.get(name=MODE_CHAT).id:
        # LLM使用部
        pass
    
    else:
        
        messages = [ messageTextFormat(RESPONSE_CHAT_NOT_STARTED) ]
        
        sendReply(messages, reply_token)


# リッチメニュー操作かテキスト入力かルートする関数
# 　リッチメニュー使用部、未実装
# user_id: string, message: string, reply_token: string

def textAction(user_id, message, reply_token):
    
    if message[0] == MESSAGE_TRIGGER:
        
        # textCommand(user_id, message, reply_token)
        pass
    
    else:
        
        textMessage(user_id, message, reply_token)


# 友だち追加関数
# 　友だち追加時にユーザーデータがなければユーザーデータを作成する
# 　追加後、メッセージを送信する
# user_id: string, reply_token: string

def createUser(user_id, reply_token):
    
    if not UserData.objects.filter(user_id=user_id).exists():
        
        UserData.objects.create(user_id=user_id)
    
    messages = [ messageTextFormat(RESPONSE_FOLLOW) ]
    
    sendReply(messages, reply_token)


# 処理ルート関数
# data: dict

def route(data):
    
    for event in data["events"]:
        
        request_type = event["type"]
        user_id = event["source"]["userId"]
        reply_token = event["replyToken"]
        
        print(event)
        
        if request_type == MESSAGE:
            
            message_type = event["message"]["type"]
            
            if message_type == TEXT:
                
                message = event["message"]["text"]
                textAction(user_id, message, reply_token)
        
        elif request_type == FOLLOW:
            
            createUser(user_id, reply_token)
