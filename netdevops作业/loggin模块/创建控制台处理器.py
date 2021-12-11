import logging


#创建日志对象
logger = logging.getLogger()
logger.setLevel("DEBUG")

#创建控制台处理器
console_handler = logging.StreamHandler()


#控制台的等级 (优先与全局等级)
console_handler.setLevel(level='INFO')

#日志器添加控制台处理器
logger.addHandler(console_handler)


logging.debug("这是debug信息")
logging.info ("这是info信息")
logging.warning("这是warning信息")
logging.error("这是error信息")
logging.critical("这是critical信息")