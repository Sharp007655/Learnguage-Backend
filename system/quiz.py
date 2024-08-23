from .constant import *
from .models import *
from .llm import *
from .messageFormat import *
from .send import *
import random
from random import choice,shuffle

#クイズ作成
def quiz_create(user_id,reply_token):
    
    word_file = []
    probability_file = []
    
    user = UserData.objects.get(user_id=user_id)
    user_word =UserWordData.objects.get(user=user.id)
    
    word_count = UserWordData.objects.get(user=user.id).count()
    
    for a in range(word_count):
        
        if user_word.period == 0 and user_word.hide == False:
            
            word_number = user_word.word
            
            word_file.append(word_number)
            probability_file.append(user_word.probability)
            
    question = choice(word_file,probability_file)
    
    
    
    return question



#クイズ出題
def quiz_question(user_id,reply_token):
    
    user = UserData.objects.get(user_id=user_id)
    
    quiz_number = quiz_create(user_id)
    
    word_data = AllWordData.objects.get(id=quiz_number)
    read = word_data.read
    
    option = options(quiz_number,read)
    
    shuffle(option)
    
    quiz_arr = []
    
    for i in (len(option)):
        
        j = i+1
        
        quiz_arr.append({ 'label': str(j) + ':' + option[i], 'text': str(j) + ':' + option[i]})
    
    messages = [ messageTextFormat(RESPONSE_QUIZ), messageQuickReplyFormat(RESPONSE_CHOOSE_LANG, quiz_arr) ]
    
    sendReply(messages, reply_token)

# [
#   { "label": "1. こんにちは", "text": "こんにちは" },
#   { "label": "2. こんばんは", "text": "こんばんは" },
# ]




# def probability_update(user_id,word_number):
    
#     user = UserData.objects.get(user_id=user_id)
#     user_word =UserWordData.objects.get(user=user.id,word=word_number)
    
#     user_word.count+=1
#     user_word.quiz+=1
    
    