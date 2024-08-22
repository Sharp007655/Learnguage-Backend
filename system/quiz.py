from .constant import *
from .models import *
import random
from random import choice

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




# [
#   { "label": "1. こんにちは", "text": "こんにちは" },
#   { "label": "2. こんばんは", "text": "こんばんは" },
# ]




# def probability_update(user_id,word_number):
    
#     user = UserData.objects.get(user_id=user_id)
#     user_word =UserWordData.objects.get(user=user.id,word=word_number)
    
#     user_word.count+=1
#     user_word.quiz+=1
    
    