# dependencies.py
from models import ChatMessage
from typing import List
from database.mongodb_manager import MongoDBManager
from datetime import datetime, timezone,timedelta
from until.time import *
class ChatHistoryDao:
    def __init__(self) -> None:
        self.storage = MongoDBManager()
    #取得历史
    def get_chat_history_for_user(self,user_name: str, last_n: int) -> List[ChatMessage]:
        where = {
            "user_name":user_name,
        }
        result = []
        for item in self.storage.find_documents(where,last_n):
            result.append(ChatMessage(type=item['type'],text=item['content']))
        return result
    #写入数据库
    def insert_chat(self,user_name:str,message:str,role:str):

        document = {
            "type":role,
            "user_name":user_name,
            "content":message,
            "date":get_now_date(),
            "timestamp":get_now_timestamp()
        }
        return self.storage.insert_document(document)
    def get_chat_count(self,user_name,date)->int:
        return self.storage.count_documents({
            "type":"user",
            "user_name":user_name,
            "date":date
        })
    
    def get_second_chat_count(self,user_name)->int:
        one_second_before = get_now_timestamp() - timedelta(seconds=1)
        return self.storage.count_documents({
            "type":"user",
            "user_name":user_name,
            "timestamp":{
                "$gte":one_second_before
            }
        })