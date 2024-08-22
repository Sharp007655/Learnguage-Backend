from .constant import *
from .models import *
import random
from random import choice

def quiz_create(user_id):
    
    word_file = []
    probability_file = []
    
    user = UserData.objects.get(user_id=user_id)
    user_word =UserWordData.objects.get(user=user.id)
    
    word_count = UserWordData.objects.get(user=user.id).count()
    
    for a in range(word_count):
        
        if user_word.period == 0:
            
            word_number = user_word.word
            
            word_file.append(word_number)
            probability_file.append(user_word.probability)
            
    question = choice(word_file,probability_file)
    
    return question