import getpass
import os
import openai
from typing import List, Optional

from pathlib import Path
from pydantic import BaseModel
from openai import OpenAI , api_key
from pydantic import BaseModel, Field

from .constant import *
from .models import *

#借り

openai.api_key = OPENAI_API_KEY

class ResponseStep(BaseModel):
    answer: str
    
client = OpenAI(api_key=OPENAI_API_KEY)


def options(user_id,word_number,read):
    
    user = UserData.objects.get(user_id=user_id)
    lang = LanguageData.objects.get(id=user.language)
    lang_ja = lang.lang_ja
    
    
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    response = client.beta.chat.completions.parse(
        model = "gpt-4o-2024-08-06",
        temperature = 0,
        
        messages = [
            {
                
                #ゴマすり
                "role" : "system",
                "content":"""あなたはとても優秀なAIです""",
                
            },
            
            {
                
                "role":"user",
                #"content":"クイズです「" + read + "」から意味は違うけど似た言葉３つなんでしょう。またその３つの言葉を　,　,　のように絶対にいれてください。「" + read + "」を含めた４つの言葉を" + lang_ja + "に翻訳したときすべて違う言葉になる必要があります。",
                "content":"あなたは学校の先生です。" + lang_ja + "を読んでそれが意味する日本語を答える四択問題を作っています。あなたは答えが「" + read + "」の問題で「" + read + "」とは意味が違う言葉を3つ作る用意する必要があります。その時上げられる言葉を3つ答えてください。またその３つの言葉を　,　,　のように絶対にいれてください。言葉以外は答えなくていいです"
                
            },

        ],
        
        response_format = ResponseStep,
        
    )

    parsed_response = response.choices[0].message.parsed
    
    option = parsed_response.answer.split(", ")
    print(option)
    option.append(read)
    
    return option