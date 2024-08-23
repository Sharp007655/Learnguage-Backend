from . import flexMessage
from .constant import *


# テキストをメッセージのオブジェクトに変換する関数
# message: string --> dict

def messageTextFormat(message, quick_reply=False):
    
    ret = {
        "type": "text",
        "text": message,
    }
    
    if quick_reply:
        
        ret["quickReply"] = {}
    
    return ret


# テキストメッセージとクイックリプライオブジェクトに変換する関数
# message: string, datas: dict > array --> dict

def messageQuickReplyFormat(message, datas):
    
    res = messageTextFormat(message, True)
    
    quick_reply = []
    
    for data in datas:
        
        quick_reply.append({
            'type': 'action',
            'action': {
                'type': 'message',
                'label': data["label"],
                'text': data["text"]
            }
        })
    
    res["quickReply"]["items"] = quick_reply
    
    return res


def flexCarouselFormat(alt_text):
    
    return {
        "type": "flex",
        "altText": alt_text,
        "contents": {
            "type": "carousel",
            "contents": []
        }
    } 


def flexFormat(alt_text):
    
    return {
        "type": "flex",
        "altText": alt_text
    } 


def messageDictionaryFormat(translate_arr):
    
    res = flexCarouselFormat(ANARYZE_RESULT)
    
    i = 0
    
    for word in translate_arr:
        
        res["contents"]["contents"].append(flexMessage.dictionary(word["source"], word["translated"], word['read']))
        
        i += 1
        if i >= 12:
            break
    
    return res


def messageTranslateFormat(translate_arr):
    
    res = flexFormat(ANARYZE_RESULT)
    
    res["contents"] = flexMessage.dictionary(translate_arr["source"], translate_arr["translated"], translate_arr['read'])
    
    return res

def messageTranslateFormat_quiz(translate_arr,datas):
    
    res = flexFormat(ANARYZE_RESULT)
    
    res["contents"] = flexMessage.dictionary_quiz(translate_arr["source"], translate_arr['read'])
    
    res["quickReply"] = {}
    quick_reply = []
    
    for data in datas:
        
        quick_reply.append({
            'type': 'action',
            'action': {
                'type': 'message',
                'label': data["label"],
                'text': data["text"]
            }
        })
    
    res["quickReply"]["items"] = quick_reply
    
    return res