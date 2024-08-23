from konlpy.tag import Okt
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
from .translate import *
from .constant import *
from .models import *


def koAnalyze(text):
    
    okt = Okt()
    
    return okt.morphs(text)


def hangulRomanize(text):
    
    transliter = Transliter(academic)
    
    return transliter.translit(text)


def addTranslatedWord(user_id, arr, source_lang):
    
    words = []
    
    lang = LanguageData.objects.get(lang_en=source_lang)
    
    user = UserData.objects.get(user_id=user_id)
    
    for word in arr:
        
        if AllWordData.objects.filter(word=word, language=lang.id).exists():
            
            word = AllWordData.objects.get(word=word, language=lang.id)
            
            dic = {
                "source": word.word,
                "translated": word.mean,
                "read": word.read,
            }
            
            if not UserWordData.objects.filter(user=user.id, word=word.id).exists():
                
                UserWordData.objects.create(user=user.id, word=word.id)
            
            else:
                
                user_word = UserWordData.objects.get(user=user.id, word=word.id)
                user_word.count += 1
                user_word.save()
        
        else:
            
            translated = translate(word, source_lang)
            
            if source_lang == KOREAN:
                read = hangulRomanize(word)
            
            new_word = AllWordData.objects.create(word=word, mean=translated, read=read, language=lang.id)
            
            UserWordData.objects.create(word=new_word.id, user=user.id)
            
            dic = {
                "source": word,
                "translated": translated,
                "read": read
            }
        
        words.append(dic)
    
    return words


def deleteSymbol(arr, symbol_arr):
    
    for symbol in symbol_arr:
        
        while symbol in arr:
            
            arr.remove(symbol)
    
    return arr


def deleteDoubleWord(before_arr):
    
    arr = []
    
    for word in before_arr:
        if not word in arr:
            arr.append(word)
    
    return arr


def formatTranslateArray(arr):
    
    arr = deleteSymbol(arr, [SYMBOL_COMMA, SYMBOL_PERIOD, SYMBOL_EXCLAMATION, SYMBOL_QUESTION, SYMBOL_EM_SPACE])
    arr = deleteDoubleWord(arr)
    
    return arr



# from soynlp import DoublespaceLineCorpus
# from soynlp.word import WordExtractor
# from soynlp.tokenizer import LTokenizer, MaxScoreTokenizer
# from .constant import *


# def koAnalyze(text):
    
#     text = "안전성에문제있는스마트폰을휴대하고탑승할경우에압수한다"
    
#     corpus = DoublespaceLineCorpus(KO_CORPUS_PATH, iter_sent=True)
    
#     word_extractor = WordExtractor()
#     word_extractor.train(corpus)
    
#     word_score = word_extractor.extract()
    
#     scores = {word:score.cohesion_forward for word, score in word_score.items()}
#     maxscore_tokenizer = MaxScoreTokenizer(scores=scores)
#     l_tokenizer = LTokenizer(scores=scores)
    
#     separates = maxscore_tokenizer.tokenize(text)
    
#     for separate in separates:
        
#         words = l_tokenizer.tokenize(separate, flatten=False)
        
