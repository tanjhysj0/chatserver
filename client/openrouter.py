import requests

import json

import openai
from openai import OpenAI
from typing import Dict,List,Tuple
from contant import *


class Openrouter:
    def __init__(self) -> None:
        self.server = "http://www.byte-way.cn"
        self.headers = {
            "HTTP-Referer": f"{self.server}", # Optional, for including your app on openrouter.ai rankings.
            "X-Title": "json", # Optional. Shows in rankings on openrouter.ai.
        }
        self.model = "openai/gpt-3.5-turbo"
        

    def send(self,app_name,message)->Tuple[str,str]:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
                "X-Title": app_name, # Optional. Shows in rankings on openrouter.ai.
            },
            data=json.dumps({
                "model": self.model,
                "messages": [
                {"role": "user", "content": message}
                ]
        })
        )
        if response.status_code!=200:
            return "","请求接口失败，反回{}".format(response.status_code)
        response_map = response.json()
        result = ""
        for item in response_map.get("choices",[]):
            result +=item.get("message",{}).get("content","")
            result+="\n"
        return result,""
