from .constant import *
from .models import *
from .messageFormat import *
from .send import *
from .quiz import *
from .analyze import *
from .chat import *


def analyze(user_id, message, language):
    
    arr = allAnalyze(message, language)
    
    arr = formatTranslateArray(arr)
    
    words = addTranslatedWord(user_id, arr, language)
    
    return words


# リッチメニュー操作時のルートをする関数（未実装）
# user_id: string, message: string, reply_token: string

def textCommand(user_id, message, reply_token):
    
    user = UserData.objects.get(user_id=user_id)
    
    if message == MESSAGE_CHAT_START:
        
        user.mode = ModeData.objects.get(name=MODE_CHAT).id
        sendReply([ messageTextFormat(RESPONSE_CHAT_START) ],reply_token)
        
    
    elif message == MESSAGE_CHAT_FINISH:
        
        user.mode = None
        ChatData.objects.filter(user = user.id).delete()
        
        sendReply([messageTextFormat(RESPONSE_CHAT_FINISH)], reply_token)
        
    elif message == MESSAGE_TRANSLATION:
        
        sendReply([ messageQuickReplyFormat( ChatData.objects.filter(user = user.id , llm = True).order_by('-order').first().message,[{ 'label': 'チャットを終了する', 'text': MESSAGE_CHAT_FINISH }])],reply_token)
    
    elif message == MESSAGE_QUIZ:
        
        user.mode = ModeData.objects.get(name=MODE_QUIZ).id
        
        quiz_question(user_id,reply_token)
    
    elif message == MESSAGE_ANALYZE:
        
        user.mode = ModeData.objects.get(name=MODE_ANALYZE).id
        
        sendReply([ messageTextFormat(RESPONSE_ANALYZE_START) ], reply_token)
    
    elif LANGUAGE_TRIGGER in message:
        
        arr = JA_LANG.keys()
        
        for lang in arr:
            
            if JA_LANG[lang] in message:
                
                user.language = LanguageData.objects.get(lang_en=lang).id
                break
        
        sendReply( [ messageTextFormat( RESPONSE_CHOOSED_LANG( JA_LANG[lang] ) ) ], reply_token )
    
    user.save()


# テキスト入力時のルートをする関数
# 　LLM使用部未実装
# 　モードが違う場合、モード変更を促すメッセージを送信
# user_id: string, message: string, reply_token: string

def textMessage(user_id, message, reply_token):
    
    user = UserData.objects.get(user_id=user_id)
    
    if user.mode == None:
        
        objects = [ messageTextFormat(RESPONSE_MENU_NOT_SELECTED) ]
        
        sendReply(objects, reply_token)
    
    elif user.mode == ModeData.objects.get(name=MODE_CHAT).id:
        
        chat_start(user_id,message,reply_token)
    
    elif user.mode == ModeData.objects.get(name=MODE_ANALYZE).id:
        
        user_language = LanguageData.objects.get(id=user.language).lang_en
        
        target = translate(message, user_language)
        
        words = analyze(user_id, message, user_language)
        
        objects = [ 
            messageTranslateFormat({ 'source': message, 'translated': target, 'read': readWordLong(message, user_language) }), 
            messageDictionaryFormat(words), 
            messageQuickReplyFormat(RESPONSE_REANALYZE, [{ 'label': '続けて分析する', 'text': MESSAGE_ANALYZE }]) 
        ]
        
        sendReply(objects, reply_token)
        
        user.mode = None
        user.save()
        
    elif user.mode == ModeData.objects.get(name=MODE_QUIZ).id:
        
        quiz_data = QuizData.objects.get(user=user.id)
        word_data = AllWordData.objects.get(id=quiz_data.word)
        
        if message == quiz_data.correct:
            judgment = RESPONSE_GOOD
            judgment_number = 1
            
        else:
            judgment = RESPONSE_BAT
            judgment_number = 0
            
        probability_update(user_id,quiz_data.word,judgment_number)
        
        objects = [
            messageTextFormat(judgment),
            messageTranslateFormat({ 'source': word_data.word, 'translated': word_data.mean, 'read': word_data.read }),
            messageQuickReplyFormat(RESPONSE_ONE_MORE_QUIZ, [{ 'label': '続けてもう一問', 'text': MESSAGE_QUIZ }]) 
        ]
        
        sendReply(objects, reply_token)
        
        user.mode = None
        user.save()
        
        quiz_data.word = None
        quiz_data.correct = None
        quiz_data.save()


# リッチメニュー操作かテキスト入力かルートする関数
# 　リッチメニュー使用部、未実装
# user_id: string, message: string, reply_token: string

def textAction(user_id, message, reply_token):
    
    if message[0] == MESSAGE_TRIGGER:
        
        textCommand(user_id, message, reply_token)
    
    else:
        
        textMessage(user_id, message, reply_token)


# 友だち追加関数
# 　友だち追加時にユーザーデータがなければユーザーデータを作成する
# 　追加後、メッセージを送信する
# user_id: string, reply_token: string

def createUser(user_id, reply_token):
    
    if not UserData.objects.filter(user_id=user_id).exists():
        
        UserData.objects.create(user_id=user_id)
    
    languages = LanguageData.objects.all()
    
    lang_arr = []
    
    for language in languages:
        
        lang_arr.append({ 'label': language.lang_ja, 'text': '> 「' + language.lang_ja + '」を学習する！' })
    
    messages = [ messageTextFormat(RESPONSE_FOLLOW), messageQuickReplyFormat(RESPONSE_CHOOSE_LANG, lang_arr) ]
    
    sendReply(messages, reply_token)


def deleteUser(user_id):
    
    user = UserData.objects.get(user_id=user_id)
    
    OriginalWordData.objects.filter(user=user.id).delete()
    
    UserWordData.objects.filter(user=user.id).delete()
    
    QuizData.objects.filter(user=user.id).delete()
    
    ChatData.objects.filter(user = user.id).delete()
    
    user.delete()


# 処理ルート関数
# data: dict

def route(data):
    
    for event in data["events"]:
        
        request_type = event["type"]
        user_id = event["source"]["userId"]
        
        if request_type == UNFOLLOW:
            
            deleteUser(user_id)
        
        else:
            
            reply_token = event["replyToken"]
            
            sendLoadingAnimation(user_id)
            
            if request_type == MESSAGE:
                
                message_type = event["message"]["type"]
                
                if message_type == TEXT:
                    
                    message = event["message"]["text"]
                    textAction(user_id, message, reply_token)
            
            elif request_type == FOLLOW:
                
                createUser(user_id, reply_token)
