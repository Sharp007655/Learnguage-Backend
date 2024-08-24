from konlpy.tag import Okt
from hangul_romanize import Transliter
from hangul_romanize.rule import academic
import nltk
from nltk.corpus import cmudict
from .translate import *
from .constant import *
from .models import *


def koAnalyze(text):
    
    okt = Okt()
    
    return okt.morphs(text)


def enAnalyze(text):
    
    if SYMBOL_EN_SPACE in text:
        
        arr = text.split(SYMBOL_EN_SPACE)
    
    else:
        
        arr = [ text ]
    
    return arr


def allAnalyze(text, language):
    
    if language == KOREAN:
        
        arr = koAnalyze(text)
    
    elif language == ENGLISH:
        
        arr = enAnalyze(text)
    
    return arr


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



def hangulRomanize(text):
    
    transliter = Transliter(academic)
    
    return transliter.translit(text)


def wordFormat(word, arr):
    
    for symbol in arr:
        
        word = word.replace(symbol, '')
    
    word = word.lower()
    
    return word

def getPronunciation(word, d):
    
    if word in d:
        
        return d[word]
    
    else:
        
        return ["(発音記号が見つかりません)"]


def replaceKeyword(text, keywords):
    
    for keyword in keywords:
        
        text = text.replace(keyword, ARPABET_TO_IPA[keyword])
        
    return text

def convertToIpa(text):
    
    text = ''.join(text)
    
    ipa_keys = ARPABET_TO_IPA.keys()
    
    text = replaceKeyword(text, ipa_keys)
    return text

def getPronunciationIpa(word, d):
    
    pronunciations = getPronunciation(word, d)
    ipa_pronunciations = [convertToIpa(pronunciation) for pronunciation in pronunciations]
    return ipa_pronunciations


def englishPronunciation(text):
    
    nltk.download('cmudict')
    
    d = cmudict.dict()
    
    return getPronunciationIpa(text, d)[0]


def readWord(text, language):
    
    if language == ENGLISH:
        
        ret = englishPronunciation(text)
    
    elif language == KOREAN:
        
        ret = hangulRomanize(text)
    
    return ret


def readWordLong(text, language):
    
    if language == ENGLISH:
        
        ret = ''
        
        text = wordFormat(text, [SYMBOL_COMMA, SYMBOL_PERIOD, SYMBOL_EXCLAMATION, SYMBOL_QUESTION, SYMBOL_EM_SPACE])
        
        arr = text.split(SYMBOL_EN_SPACE)
        
        for word in arr:
            
            ret += englishPronunciation(word) + SYMBOL_EN_SPACE
    
    elif language == KOREAN:
        
        ret = hangulRomanize(text)
    
    return ret


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
            
            if source_lang == ENGLISH:
                
                word = wordFormat(word, [SYMBOL_COMMA, SYMBOL_PERIOD, SYMBOL_EXCLAMATION, SYMBOL_QUESTION, SYMBOL_EM_SPACE])
            
            translated = translate(word, source_lang)
            
            if source_lang == KOREAN:
                read = hangulRomanize(word)
            
            elif source_lang == ENGLISH:
                read = englishPronunciation(word)
            
            new_word = AllWordData.objects.create(word=word, mean=translated, read=read, language=lang.id)
            
            UserWordData.objects.create(word=new_word.id, user=user.id)
            
            dic = {
                "source": word,
                "translated": translated,
                "read": read
            }
        
        words.append(dic)
    
    return words
