from database.chat_history_dao import ChatHistoryDao
from client.openrouter import Openrouter 
from typing import List
from models import *
from datetime import datetime, timezone,timedelta
from requests import Response
from service.log_service import getLog
from typing import Tuple,List
class ChatService:
    def __init__(self) -> None:
        self.chat_history_dao = ChatHistoryDao()
        self.openrouter = Openrouter()
        self.log = getLog()
    def get_ai_chat_response(self,request:AIChatRequest)->Tuple[str,str]:
        #取得AI的回复
        MAX_TOKENS = 8192
        APPROX_TOKEN_LENGTH = 4  # This is an estimation, adjust based on the actual language model
        # If the request is too long, we trim it
        trimmed_message = self.middle_out_text(request.message, MAX_TOKENS, APPROX_TOKEN_LENGTH)
        replay_response,err =  self.openrouter.send(request.user_name,trimmed_message)
        if err!="":
            self.log.warning("请求回签失败")
            return "",err
        
        self.log.info("请求回答成功:{}".format(replay_response))
        #先写入用户的消息
        self.chat_history_dao.insert_chat(request.user_name,request.message,"user")
    
        
        #再来写入AI的回复
        self.chat_history_dao.insert_chat(request.user_name,replay_response,"ai")
        self.log.info("记录数据库成功")
        return replay_response,""

    def get_user_chat_history(self,request:UserChatHistoryRequest)->List[ChatMessage]:
        return self.chat_history_dao.get_chat_history_for_user(request.user_name,request.last_n)

    
    def get_chat_status_today(self,request:UserStatusRequest)->int:
        return self.chat_history_dao.get_chat_count(request.user_name,datetime.now(timezone.utc).strftime("%Y-%m-%d"))

    def middle_out_text(self,text: str, max_tokens: int, approx_token_length: int) -> str:
        """
        Return text after removing middle part to fit within max_tokens, assuming
        approx_token_length characters per token.
        """
        max_chars = max_tokens * approx_token_length
        text_length = len(text)
        
        if text_length <= max_chars:
            # No need to trim the text if it's already within the limit
            return text
        
        # Calculate half of the excess length to trim from the middle
        chars_to_trim = text_length - max_chars
        trim_start = text_length // 2 - chars_to_trim // 2
        trim_end = trim_start + chars_to_trim
        
        # Trim the text from the middle
        trimmed_text = text[:trim_start] + text[trim_end:]
        
        return trimmed_text