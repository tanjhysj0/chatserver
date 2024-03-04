from models import ChatMessage
from datetime import datetime
from database.chat_history_dao import ChatHistoryDao
import unittest
from unittest.mock import MagicMock

class TestChatHistoryDao(unittest.TestCase):

    def setUp(self):
        # 创建Mock对象替代MongoDBManager
        self.mock_mongo_manager = MagicMock()
        # 将Mock的MongoDBManager传递给ChatHistory实例
        self.chat_history = ChatHistoryDao()
        self.chat_history.storage = self.mock_mongo_manager

    def test_get_chat_history_for_user(self):
        # 假设的数据返回值
        mock_chat_messages = [
            {
                "user_name":"jason",
                "type":"user",
                "content":"I am serlon",
                "timestamp":"2024-02-27 12:00:00"
            }
        ]
        # 配置mock对象返回假数据
        self.mock_mongo_manager.find_documents.return_value = mock_chat_messages        
        # 调用方法
        result = self.chat_history.get_chat_history_for_user("jason", 2)

        # 测试返回值是否如我们所模拟的一样
        self.assertEqual(result, [
            ChatMessage(type="user",text="I am serlon")
        ])


    def test_insert_chat(self):
        # 设置这个测试不应该有任何返回值（insert_document是“None”）
        self.mock_mongo_manager.insert_document.return_value = True
        
        # 调用插入方法
        result = self.chat_history.insert_chat("johndoe", "hey there","user")

        self.assertTrue(result)
    def test_get_chat_status_today(self):
        self.mock_mongo_manager.count_documents.return_value = 120
        self.assertEqual(self.chat_history.get_chat_count("jason",datetime.now().date().strftime("%Y-%m-%d")),120)