from .constant import *
import deepl, os

def translate(text, source_lang, target_lang=JAPANESE):
    
    auth_key = os.environ.get("DEEPL_API_KEY")
    
    translator = deepl.Translator(auth_key)
    
    result = translator.translate_text(text=text, target_lang=target_lang, source_lang=source_lang)
    
    return result.text
