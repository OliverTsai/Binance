
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import time
import Candlestick as candlestick
import pandas as pd
import re

def init_time():
    yesterdayTime = int(time.time()) - 86400
    str_time = time.localtime(yesterdayTime)
    timeString = time.strftime("%Y-%m-%d %H:%M:%S", str_time)
    yesterday = timeString[0:10]
    init_time = " 08:00:00"
    yesterday = yesterday + init_time
    return yesterday

def get_candlestick_new(symbol="BTCUSDT",interval = '1h',limit=500, filename=""):
    start = init_time()
    # end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    candlestick.get_candlestick_data_2(symbol=symbol,startTimeStr=start,interval=interval, limit=limit, filename=filename)

if __name__ == '__main__':
    get_candlestick_new(interval = '5m',limit=500,filename="CSV/Candlestick_5m.csv")