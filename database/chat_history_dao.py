# dependencies.py
from models import ChatMessage
from typing import List
from database.mongodb_manager import MongoDBManager
from datetime import datetime, timezone,timedelta
class ChatHistoryDao:
    def __init__(self) -> None:
        self.storage = MongoDBManager()

    def get_now_timestamp(self):
        return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8)))
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
        current_time = self.get_now_timestamp()
        document = {
            "type":role,
            "user_name":user_name,
            "content":message,
            "date":current_time.date().strftime("%Y-%m-%d"),
            "timestamp":current_time
        }
        return self.storage.insert_document(document)
    def get_chat_count(self,user_name,date)->int:
        return self.storage.count_documents({
            "user_name":user_name,
            "date":date
        })
    
    def get_second_chat_count(self,user_name)->int:
        current_time = self.get_now_timestamp()

        one_second_before = current_time - timedelta(seconds=1)
        return self.storage.count_documents({
            "user_name":user_name,
            "timestamp":{
                "$gte":one_second_before
            }
        })