
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import time
import Candlestick as candlestick
import pandas as pd
import re

def start_time(interval):
    readCsv = pd.read_csv('CSV/LongShortAcc_close_'+interval+'.csv')
    lines = readCsv.openTime
    line  = str(lines.tail(1))
    dataFormat = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
    result = dataFormat.findall(line)
    return result[0]

def get_candlestick_new(symbol="BTCUSDT",interval = '1h',limit=500, filename=""):
    start = start_time(interval)
    # end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    candlestick.get_candlestick_data_2(symbol=symbol,startTimeStr=start,interval=interval, limit=limit, filename=filename)


if __name__ == '__main__':
    get_candlestick_new(interval = '5m',limit=500,filename="CSV/a.csv")
    