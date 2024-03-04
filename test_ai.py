import requests
import json
OPENROUTER_API_KEY = "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"
YOUR_SITE_URL = "www.byte-way.cn"
YOUR_APP_NAME = "I set name"
def test_ai():


    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
        "X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "openai/gpt-3.5-turbo", # Optional
        "messages": [
        {"role": "user", "content": "What is the meaning of life?"}
        ]
    })
    )
    assert response.status_code==200
    print(response)