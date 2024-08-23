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


def options(word_number,read):
    
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
                "content":"「" + read + "」から意味は違うけど似た言葉３つなんでしょう。またその３つの言葉を　,　,　のようにいれてください。意味は答えなくていいです。",
                
            },

        ],
        
        response_format = ResponseStep,
        
    )

    parsed_response = response.choices[0].message.parsed
    
    option = parsed_response.answer.split(", ")
    
    option.append(read)
    
    return option