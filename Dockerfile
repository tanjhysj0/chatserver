# 使用官方Python镜像作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制requirements.txt文件到容器中
COPY requirements.txt .

# 安装requirements.txt中定义的所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将本地代码复制到容器的工作目录中
COPY . .

# 暴露容器将要监听的端口，假设是8000
EXPOSE 80

# 设置环境变量，用于Uvicorn
ENV HOST=0.0.0.0
ENV PORT=80

# 在容器启动时运行Uvicorn服务器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
