from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
import time
import LongShortAccounts as longShortAccounts
import pandas as pd
import re
import datetime

def start_time_obj(interval):

    readCsv = pd.read_csv('CSV/LongShortAcc_close_'+interval+'.csv')
    lines = readCsv.openTime
    line  = str(lines.tail(1))
    dataFormat = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
    result = dataFormat.findall(line)
    return datetime.datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S")

def add_time(startObj, interval = '5m'):

    if interval == '5m':
        time_change = datetime.timedelta(minutes=5)
    elif interval == '30m':
        time_change = datetime.timedelta(minutes=30)
    elif interval == '1h':
        time_change = datetime.timedelta(hours=1)
    elif interval == '4h':
        time_change = datetime.timedelta(hours=4)
    elif interval == '6h':
        time_change = datetime.timedelta(hours=6)
    elif interval == '1d':
        time_change = datetime.timedelta(days=1)
    
    return startObj + (time_change*499)

def get_top_long_short_new(symbol="BTCUSDT", period="5m", limit=500, filename=""):
    startObj = start_time_obj(period)
    endObj   = add_time(startObj, period)
    longShortAccounts.get_top_long_short_accounts_2(symbol=symbol, startTimeStr = str(startObj), endtimeStr=str(endObj), limit = limit, period=period, filename=filename)

if __name__ == '__main__':
    get_top_long_short_new(period='5m',limit=500,filename="CSV/a.csv")