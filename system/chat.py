from .models import *
from .llm import *
from .translate import *
from .constant import *
from .messageFormat import *
from .send import *



def chat_start(user_id,message,reply_token):
    
    user = UserData.objects.get(user_id=user_id)
    lang = LanguageData.objects.get(id=user.language)
    lang_je = lang.lang_en
    
    answer = chat_reply(user_id,message)
    
    answer_translate = translate(answer,JAPANESE,lang_je)
    
    sendReply([ messageTextFormat(answer_translate) , messageQuickReplyFormat(answer,[{ 'label': 'チャットを終了する', 'text': MESSAGE_CHAT_FINISH }])],reply_token)