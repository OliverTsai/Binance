
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
import time
from datetime import datetime
import csv

def ts_to_date(ts , fmt_str):
    timestamp = ts/1000
    date_time = datetime.fromtimestamp(timestamp)
    dte_str = date_time.strftime(fmt_str)
    return dte_str

def date_to_ts(dte , frm_str):
    datetime_obj = datetime.strptime(dte, frm_str)
    obj_ts = int(time.mktime(datetime_obj.timetuple()) * 1000)
    return str(obj_ts)


def get_top_long_short_accounts(symbol="BTCUSDT", startTimeStr = '', endtimeStr='', limit = 500, period='5m'):
    startTime = date_to_ts(startTimeStr, "%Y-%m-%d %H:%M:%S")
    endtime   = date_to_ts(endtimeStr, "%Y-%m-%d %H:%M:%S")

    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_top_long_short_accounts(symbol, period=period, startTime=startTime, endTime=endtime, limit=limit)


    with open('LongShortAccounts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['longAccount','longShortRatio','shortAccount','symbol','timestamp'])
        for r in result:
            day = ts_to_date(r.timestamp,"%Y-%m-%d %H:%M:%S")
            writer.writerow([r.longAccount , r.longShortRatio ,r.shortAccount , r.symbol,day])


def get_top_long_short_accounts_2(symbol="BTCUSDT", startTimeStr = '', endtimeStr='', limit = 500, period='5m', filename=""):
    startTime = date_to_ts(startTimeStr, "%Y-%m-%d %H:%M:%S")
    endtime   = date_to_ts(endtimeStr, "%Y-%m-%d %H:%M:%S")

    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_top_long_short_accounts(symbol, period=period, startTime=startTime, endTime=endtime, limit=limit)


    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['longAccount','longShortRatio','shortAccount','symbol','timestamp'])
        for r in result:
            day = ts_to_date(r.timestamp,"%Y-%m-%d %H:%M:%S")
            writer.writerow([r.longAccount , r.longShortRatio ,r.shortAccount , r.symbol,day])

if __name__ == '__main__':
    get_top_long_short_accounts_2(startTimeStr='2021-08-28 14:00:00', endtimeStr='2021-08-29 14:00:00',period='5m', limit = 500,filename ="CSV/LongShortAccounts_5m.csv")

# interval
# MIN1 = "1m"
# MIN3 = "3m"
# MIN5 = "5m"
# MIN15 = "15m"
# MIN30 = "30m"
# HOUR1 = "1h"
# HOUR2 = "2h"
# HOUR4 = "4h"
# HOUR6 = "6h"
# HOUR8 = "8h"
# HOUR12 = "12h"
# DAY1 = "1d"
# DAY3 = "3d"
# WEEK1 = "1w"
# MON1 = "1m"