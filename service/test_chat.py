import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from service.chat_service import ChatService
from models import *
from client.openrouter import Openrouter
import requests
from requests.models import Response
class TestChat(unittest.TestCase):
    def setUp(self):
        # 创建Mock对象替代MongoDBManager
        self.mock_mongo_manager = MagicMock()

        # 将Mock的MongoDBManager传递给ChatHistory实例
        self.chat_service = ChatService()
        self.chat_service.chat_history_dao.storage = self.mock_mongo_manager
        
        self.mock_openrouter = MagicMock()
        self.chat_service.openrouter =self.mock_openrouter

    def test_get_ai_chat_response(self):
        # 创建模拟请求和响应
        mock_request = AIChatRequest(user_name="test_user", message="this is a test message")


        self.mock_openrouter.send.return_value = ("this is a mock response from AI","")

        # 调用方法
        response,err = self.chat_service.get_ai_chat_response(mock_request)
        


        # 断言响应是预期的结果 (这取决于send方法实际如何处理请求)
        self.assertEqual(response, "this is a mock response from AI")

        self.assertEqual(err, "")


    def test_get_user_chat_history(self):
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


        request = UserChatHistoryRequest(user_name="jason",last_n=120)
        chat_history = self.chat_service.get_user_chat_history(request)

        self.assertEqual(chat_history,[
            ChatMessage(text="I am serlon",type="user")
        ])

    def test_get_chat_status_today(self):

        request = UserStatusRequest(user_name="jason")
        self.chat_service.chat_history_dao.storage.count_documents.return_value = 9
        self.assertEqual(self.chat_service.get_chat_status_today(request),9)
        

