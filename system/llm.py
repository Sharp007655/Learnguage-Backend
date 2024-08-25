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
                "content":"""あなたはとても優秀なAIです。３つの言葉を　,　,　のように絶対にいれてください。言葉以外は答えなくていいです""",
                
            },
            
            {
                
                "role":"user",
                "content":"あなたは学校の先生です。" + lang_ja + "を読んでそれが意味する日本語を答える四択問題を作っています。あなたは答えが「" + read + "」の問題で「" + read + "」とは意味が違う言葉を3つ作る用意する必要があります。その時上げられる言葉を3つ答えてください。"
                
            },

        ],
        
        response_format = ResponseStep,
        
    )

    parsed_response = response.choices[0].message.parsed
    
    option = parsed_response.answer.split(", ")
    
    option.append(read)
    
    return option





def chat_reply(user_id,message):
    
    user = UserData.objects.get(user_id=user_id)
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    if not ChatData.objects.filter(user=user.id).exists():
        
        chat_data_count = 0
        
        response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        temperature=0,
        
        messages=[
            {
                "role": "system",
                "content": """あなたは送信者の友達です。あなたは絶対に１文で返答してください。日本語で返答してください。返答した文を「」で囲まないでください。漢字含めて30文字以内で会話のように返答してください。どうしても30字超えそうな時は要約して返してください。文章以外は答えないでください。"""
            },
            {
                "role": "user",
                "content": message
            },
            
            {
                "role": "assistant",
                "content": "返答"
            },
        ],
        
        response_format = ResponseStep,
        
        )
        
    else:
        
        messages_list =[
            {
                    "role": "system",
                    "content": """あなたは送信者の友達です。あなたは絶対に１文で返答してください。日本語で返答してください。返答した文を「」で囲まないでください。漢字含めて30文字以内で会話のように返答してください。どうしても30字超えそうな時は要約して返してください。文章以外は答えないでください。"""
            },
        ]
        
        chat_data = ChatData.objects.filter(user = user.id).order_by('order')
        chat_data_number = chat_data.first().order
        chat_data_count = chat_data.filter(llm = True).count()
        
        for a in range(chat_data_count):
            
            c = chat_data_number + a
            
            user_message = chat_data.filter(llm = False, order = c).first().message
            llm_message = chat_data.filter(llm = True, order = c).first().message
            
            messages_list.append(
                {
                    "role": "user",
                    "content": user_message
                },
            )
            
            messages_list.append(
                {
                    "role": "assistant",
                    "content": llm_message
                },
            )
        
        messages_list.append(
            {
                "role": "user",
                "content": message
            },
        )
        
        messages_list.append(
            {
                "role": "assistant",
                "content": "返答"
            },
        )
    
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            temperature=0,
            
            messages = messages_list,
            
            response_format = ResponseStep,
            
        )

    # レスポンスから内容を取り出して表示
    parsed_response = response.choices[0].message.parsed
    
    ChatData.objects.create(user = user.id,message = message,llm = False,order = chat_data_count)
    ChatData.objects.create(user = user.id,message = parsed_response.answer,llm = True,order = chat_data_count)
    
    chat_amount(user_id)
    
    return parsed_response.answer




def chat_amount(user_id):
    
    user = UserData.objects.get(user_id=user_id)
    chat_data = ChatData.objects.filter(user=user.id).order_by('-order')
    
    chat_count = chat_data.filter(llm = True).count()
    chat_number = chat_data.last().order
    
    if chat_count == 10:
        
        client = OpenAI(api_key=OPENAI_API_KEY)
    
        response = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": """あなたはとても優秀なAIです。あなたは絶対に１文で返答してください。日本語で返答してください。返答した文を「」で囲まないでください。漢字含めて30文字以内で会話のように返答してください。どうしても30字超えそうな時は要約して返してください。文章以外は答えないでください。"""
                },
                {
                    "role": "user",
                    "content": chat_data.filter(llm = False,order = chat_number).first().message
                },
                {
                    "role": "assistant",
                    "content": chat_data.filter(llm = True,order = chat_number).first().message
                },
                {
                    "role": "user",
                    "content": chat_data.filter(llm = False,order = chat_number + 1).first().message
                },
                {
                    "role": "assistant",
                    "content": chat_data.filter(llm = True,order = chat_number + 1).first().message
                },
                {
                    "role": "user",
                    "content": "今までの会話を要約してください"
                },
                {
                    "role": "assistant",
                    "content": "返答"
                },
            ],
            
            response_format = ResponseStep,
            
        )
        
        parsed_response = response.choices[0].message.parsed
        
        ChatData.objects.filter(user = user.id,order = chat_number).delete()
        ChatData.objects.filter(user = user.id,order = chat_number + 1).delete()
        
        ChatData.objects.create(user = user.id,message = parsed_response.answer,llm = False,order = chat_number + 1)
        ChatData.objects.create(user = user.id,message = parsed_response.answer,llm = True,order = chat_number + 1)