import logging

class Log():
    
    def __init__(self,level="DEBUG"):
        #日志对象

        self.log = logging.getLogger()
        self.log.setLevel("DEBUG")


    def console_handle(self,level="DEBUG"):
        """控制台处理器"""
        console_handle = logging.StreamHandler()
        console_handle.setLevel(level)

        #处理器添加格式器
        console_handle.setFormatter(self.get_formatter()[0])
        return console_handle


    def file_handle(self,level="DEBUG"):
        """文件处理"""

        file_handler = logging.FileHandler("log3.txt",mode="a",encoding="utf8")
        file_handler.setLevel(level)
        #处理器添加格式
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler

    def get_formatter(self):
        """格式器"""

        #定义输出格式
        console_fmt = logging.Formatter(fmt="%(name)s---->%(levelname)s----->%(asctime)s")
        file_fmt = logging.Formatter("%(name)s---->%(asctime)s----->%(levelname)s----->%(message)s")
        return console_fmt,file_fmt


    def get_log(self):
        #日志器添加控制台处理器
        self.log.addHandler(self.console_handle())
        #日志器添加文件处理
        self.log.addHandler(self.file_handle())
        return self.log


log = Log()
logger = log.get_log()
logger.info("第一条信息")
logger.info("第二条信息")