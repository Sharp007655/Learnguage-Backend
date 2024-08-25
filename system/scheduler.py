from .models import *
from .quiz import *
from apscheduler.schedulers.background import BackgroundScheduler


def quizSend():
    
    users = UserData.objects.all()
    
    for user in users:
        
        if not UserWordData.objects.filter(user=user.id).exists():
            continue
        
        user.mode = ModeData.objects.get(name=MODE_QUIZ).id
        user.save()
        
        quiz_question(user.user_id)


def triggerSet():
    
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(quizSend, 'cron', hour=7, minute=0)
    
    scheduler.start()
