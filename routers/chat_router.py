# routers/chat.py
from fastapi import APIRouter, HTTPException
from typing import List
from models import *
from service.chat_service import ChatService
from fastapi import HTTPException, status
import traceback

router = APIRouter()

@router.post("/get_ai_chat_response", response_model=AIChatResponse)
async def get_ai_chat_response(request: AIChatRequest)->AIChatResponse:

    try:
        server = ChatService()
        replay_response,err =  server.get_ai_chat_response(request)
        if err!="":
            return AIChatResponse(msg=err,code=500,response="")
        return AIChatResponse(msg=err,code=200,response=replay_response)
    except Exception as ex:
        stack_trace = traceback.format_exc()
        print(stack_trace)
        return AIChatResponse(msg=str(ex),code=500,response="")

@router.post("/get_user_chat_history", response_model=UserChatHistoryResponse)
async def get_user_chat_history(request: UserChatHistoryRequest)->UserChatHistoryResponse:
    try:
        server = ChatService()
        return UserChatHistoryResponse(
            code=200,
            msg="请求成功",
            response=server.get_user_chat_history(request)
        ) 
    except Exception as ex:
        stack_trace = traceback.format_exc()
        print(stack_trace)
        return UserChatHistoryResponse(msg=str(ex),code=500,response=[])

@router.post("/get_chat_status_today",response_model=UserStatusResponse)
async def get_chat_status_today(request:UserStatusRequest)->UserStatusResponse:
    try:
        server = ChatService()

        return UserStatusResponse(
            code=200,
            msg="请求成功",
            response=UserStatus(
                user_name=request.user_name,
                chat_cn=server.get_chat_status_today(request)
            )
        )
    except Exception as ex:
        stack_trace = traceback.format_exc()
        print(stack_trace)
        return UserStatusResponse(msg=str(ex),code=500)