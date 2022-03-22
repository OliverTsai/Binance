from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import time
from datetime import datetime
import csv





def init_time():
    yesterdayTime = int(time.time()) - 86400
    str_time = time.localtime(yesterdayTime)
    timeString = time.strftime("%Y-%m-%d %H:%M:%S", str_time)
    yesterday = timeString[0:10]
    init_time = " 08:00:00"
    yesterday = yesterday + init_time
    return yesterday





if __name__ == '__main__':
    # date_to_ts(ti , "%Y-%m-%d %H:%M:%S")
    init_time()