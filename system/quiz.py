from .constant import *
from .models import *
from .llm import *
from .messageFormat import *
from .send import *
import random
from random import choices,shuffle

#クイズ作成
def quiz_create(user_id):
    
    word_file = []
    probability_file = []
    
    user = UserData.objects.get(user_id=user_id)
    user_word =UserWordData.objects.filter(user=user.id)
    
    for word_id in user_word:
        
        if word_id.period == 1 and word_id.hide == False:
            
            word_number = word_id.word
            
            word_file.append(word_number)
            probability_file.append(word_id.probability)
            
    question = choices(word_file,weights=probability_file,k=1)[0]
    
    return question



#クイズ出題
def quiz_question(user_id, reply_token=None):
    
    user = UserData.objects.get(user_id=user_id)
    
    quiz_number = quiz_create(user_id)
    
    word_data = AllWordData.objects.get(id=quiz_number)
    mean = word_data.mean
    read = word_data.read
    word = word_data.word
    
    option = options(user_id,quiz_number,mean)
    
    shuffle(option)
    
    correct_number = option.index(mean) + 1
    
    quiz_arr = []
    
    for i in option:
        
        j = option.index(i)
        
        quiz_arr.append({ 'label': str(j+1) + '.' + i, 'text': str(j+1) + ' ' + i})
        
        # quiz_arr.append({ 'label': str(j) + ':' + option[i], 'text': str(j) + ':' + option[i]})
    
    messages = []
    
    if reply_token == None:
        messages.append( messageTextFormat(RESPONSE_DAIRY_QUIZ) )
    
    messages += [ messageTextFormat(RESPONSE_QUIZ), messageTranslateFormat_quiz({'source':word,'read':read}, quiz_arr) ]
    
    if reply_token == None:
        
        sendPushMessage(messages, user_id)
    
    else:
        
        sendReply(messages, reply_token)
    
    
    if not QuizData.objects.filter(user=user.id).exists():
        
        QuizData.objects.create(user=user.id)
        
    quiz_data = QuizData.objects.get(user=user.id)
    
    quiz_data.correct = str(correct_number) + ' ' + mean
    quiz_data.word = quiz_number
    quiz_data.save()
    

# [
#   { "label": "1. こんにちは", "text": "こんにちは" },
#   { "label": "2. こんばんは", "text": "こんばんは" },
# ]



#確率などの計算

def probability_update(user_id,word_number,judgment):
    
    user = UserData.objects.get(user_id=user_id)
    user_word =UserWordData.objects.filter(user=user.id)
    user_word_quiz = user_word.get(word = word_number)
    
    user_word_quiz.count += 1
    user_word_quiz.quiz += 1
    user_word_quiz.correct += judgment
    
    user_word_quiz.probability = user_word_quiz.quiz/user_word_quiz.correct
    
    user_word_count = user_word.count()
    
    #print(user_word_count)
    
    for word in user_word:
        
        if word.period == 1:
            
            pass
        
        else:
            
            word.period -= 1
            
        word.save()
    
    if user_word_count < 21:
        
        user_word_quiz.period = user_word_count
        
    else:
        
        user_word_quiz.period = 21
        
    user_word_quiz.save()