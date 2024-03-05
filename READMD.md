
# 安装启动说明

+ python3.11环境下
``` shell
pip install --no-cache-dir -r requirements.txt
uvicorn main:app --host  0.0.0.0  --port  80 --reload
```
+ docker启动
``` shell
docker-compose up
```
+ 运行单元测试
``` jason
pytest
```

# API接口说明
下面的请求接口全要根上http://{base_url}
当前测试地址为:http://120.76.241.138
### 发送消息
#### 请求地址
> /get_ai_chat_response
#### 请求方式
> POST
#### 请求参数
``` json
{
    "user_name":"jason1",
    "message":"请问刚刚我问你什么问题了？"
}
```
### 响应参数
``` json
    "msg": "localhost:27017: [Errno 111] Connection refused ",
    "code": 500,
    "response": "正确时这里是正确的回答"
```

### 取得历史聊天记录
#### 请求地址
> /get_user_chat_history
#### 请求方式
> POST
#### 请求参数
``` json
{
    "user_name":"jason",
    "last_n":10
}
```
### 响应参数
``` json
{
    "msg": "请求成功",
    "code": 200,
    "response": [
        {
            "type": "ai",
            "text": "您问我什么问题了？\n"
        },
        {
            "type": "user",
            "text": "请问刚刚我问你什么问题了？"
        }
    ]
}
```
## 查看今天的聊天统计
#### 请求地址
> /get_chat_status_today
#### 请求方式
> POST
#### 请求参数
``` json
{
    "user_name":"jason1"

}
```

#### 响应参数
``` json
{
    "msg": "请求成功",
    "code": 200,
    "response": {
        "user_name": "jason1",
        "chat_cn": 2
    }
}
```