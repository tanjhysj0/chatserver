import logging

def getLog():
    # 创建一个日志记录器
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 创建一个Handler来将日志写入文件
    file_handler = logging.FileHandler('my_log.log')  # 日志将被写入到这个文件中
    file_handler.setLevel(logging.DEBUG)  # 设置文件Handler的日志级别

    # 创建一个Handler来将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 设置控制台Handler的日志级别

    # 创建一个格式器，并将其添加到Handler中
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将Handler添加到日志记录器logger中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger