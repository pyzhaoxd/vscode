
import logging

#默认输入等级是warning

#时间格式
fmt = "%(name)s----->%(message)s------>%(asctime)s"
logging.basicConfig(level="DEBUG",format=fmt)

logging.debug("这是debug信息")
logging.info ("这是info信息")
logging.warning("这是warning信息")
logging.error("这是error信息")
logging.critical("这是critical信息")