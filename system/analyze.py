from konlpy.tag import Okt
from .translate import *
from .constant import *


def koAnalyze(text):
    
    okt = Okt()
    
    return okt.morphs(text)


def addTranslatedWord(arr, source_lang):
    
    words = []
    
    for word in arr:
        
        words.append(
            {
                "source": word,
                "translated": translate(word, source_lang)
            }
        )
    
    return words


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
        
