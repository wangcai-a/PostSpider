import logging
import getpass
import sys

'''
        我们知道，世界上存在着已知的已知事物，也就是说有些事情我们知道自己知道，
    而我们也知道世上存在着被人所知的不明事物，这就是说有些事情我们知道自己不知道。
    同时，世上还存在着我们不知道的不明事物，也就是说我们不知道自己不知道。
'''

## 定义mylog类=
class Mylog(object):
## 类Mylog的构造函数
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

## 日志文件名
        # sys.argv[]获取程序从外部输入的参数  [文件路径, 参数1, 参数2, ...]
        self.logFile = sys.argv[0][0:-3] + '.log'
        self.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")


## 日志显示到屏幕上并输出到日志文件内
        self.logHand = logging.FileHandler(self.logFile, encoding='utf-8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        self.logHandSt = logging.StreamHandler()
        self.logHandSt.setFormatter(self.formatter)
        self.logHandSt.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)

## 日志的5个级别对应的一下5个函数
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__=="__main__":
    mylog = Mylog()
    mylog.debug('I.m debug')
    mylog.info('I.m info')
    mylog.warning('I.m warning')
    mylog.error('I.m error')
    mylog.critical('I.m critical')