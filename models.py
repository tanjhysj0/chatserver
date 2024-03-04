from pydantic import BaseModel
from typing import List
class AIChatRequest(BaseModel):
    message: str
    user_name: str

class AIChatResponse(BaseModel):
    msg:str
    code:int
    response: str|None=None

class ChatMessage(BaseModel):
    type: str
    text: str
class UserChatHistoryRequest(BaseModel):
    user_name:str
    last_n:int

class UserChatHistoryResponse(BaseModel):
    msg:str
    code:int
    response:List[ChatMessage]|None=None    



class UserStatusRequest(BaseModel):
    user_name:str

class UserStatus(BaseModel):
    user_name:str
    chat_cn:int
class UserStatusResponse(BaseModel):
    msg:str
    code:int
    response:UserStatus|None=None
