import logging



#第一步：创建日志器
logger = logging.getLogger("system")
logger.setLevel("DEBUG")

#第二步：定义处理器。控制台合文本输出两种方式
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log2.txt",mode="a",encoding="utf8")


#控制台的等级 (优先与全局等级)
file_handler.setLevel(level='INFO')



#第三步：设置不同的输出格式
console_fmt = "%(name)s---->%(levelname)s----->%(asctime)s"
file_fmt = "%(name)s---->%(asctime)s----->%(levelname)s"


#第三步：格式
fmt1= logging.Formatter(fmt=console_fmt)
fmt2 = logging.Formatter(fmt=file_fmt)


console_handler.setFormatter(fmt1)
file_handler.setFormatter(fmt2)

#日志器添加控制台处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#日志输出
logging.debug("这是debug信息")
logging.info ("这是info信息")
logging.warning("这是warning信息")
logging.error("这是error信息")
logging.critical("这是critical信息")

