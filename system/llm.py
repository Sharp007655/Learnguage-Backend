import getpass
import os
import openai
from typing import List, Optional

from pathlib import Path
from pydantic import BaseModel
from openai import OpenAI , api_key
from pydantic import BaseModel, Field

from .constant import *

#借り

openai.api_key = OPENAI_API_KEY

class ResponseStep(BaseModel):
    answer: str
    
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
            "content":"「農林水産省」から意味は違うけど似た言葉３つなんでしょう。またその３つの言葉を　,　,　のようにいれてください。意味は答えなくていいです。",
            
        },

    ],
    
    response_format = ResponseStep,
    
)

#response.choices[0].message.parsed.steps

parsed_response = response.choices[0].message.parsed
#print(parsed_response.step)
print(parsed_response.answer)

print(parsed_response.answer.split(", "))

