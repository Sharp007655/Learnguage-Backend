# テキストをメッセージのオブジェクトに変換する関数
# message: string --> dict

def messageTextFormat(message):
    
    return {
        "type": "text",
        "text": message
    }


# テキストメッセージとクイックリプライオブジェクトに変換する関数
# message: string, datas: dict > array --> dict

def messageQuickReplyFormat(message, datas):
    
    res = messageTextFormat(message)
    
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
