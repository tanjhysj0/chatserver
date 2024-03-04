from pymongo import MongoClient
from typing import List
class MongoDBManager:
    def __init__(self, host='localhost', port=27017, db_name='chat_bot', collection_name='chat_history'):
        # 初始化MongoDB连接
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def insert_document(self, document):
        """插入单个文档到集合中"""
        if isinstance(document, dict):
            return self.collection.insert_one(document).inserted_id
        else:
            raise TypeError("document must be an instance of dict")

    def insert_documents(self, documents):
        """插入多个文档到集合中"""
        if isinstance(documents, list):
            return self.collection.insert_many(documents).inserted_ids
        else:
            raise TypeError("documents must be an instance of list of dicts")
    def count_documents(self,query)->int:
        return self.collection.count_documents(query)
    def find_document(self, query):
        """查询集合中的文档，参数query是一个字典"""
        return self.collection.find_one(query)
    
    def find_documents(self, query:dict,limit:int):
        """查询集合中的多个文档，参数query是一个字典"""
        return self.collection.find(query).sort({"timestamp":-1}).limit(limit)