"""
Python之日志处理（logging模块）
https://www.cnblogs.com/yyds/p/6901864.html
"""
import logging

logging.basicConfig(level=logging.DEBUG)

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
# # 上方代码等同于下方代码
# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.INFO, "This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL, "This is a critical log.")


# 一个例子：在日志消息中添加exc_info和stack_info信息，并添加两个自定义的字端 ip和user
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#
# logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})


# 现在有以下几个日志记录的需求：
#
# 1）要求将所有级别的所有日志都写入磁盘文件中
# 2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
# 3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
# 4）要求all.log在每天凌晨进行日志切割
# import logging
# import logging.handlers
# import datetime
#
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
# f_handler = logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')