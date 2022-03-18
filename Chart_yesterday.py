import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time
from matplotlib.dates import WeekdayLocator, DayLocator, MONDAY


def date_to_ts(dte , frm_str):
    datetime_obj = datetime.strptime(dte, frm_str)
    obj_ts = int(time.mktime(datetime_obj.timetuple()) * 1000)
    return str(obj_ts)

def chart(day = '1h',linit = 100):
    list_dataA = []
    list_dataB = []
    list_time = []
    read = pd.read_csv('CSV/LongShortAcc_close_'+day+'.csv')
    read = read.tail(linit)

    for i in read.shortAccount:
        list_dataA.append(i)
    
    for r in read.close:
        list_dataB.append(r)

    for k in read.openTime:
        list_time.append(k[5:16])
    
    x = list_time
    y1 = list_dataA
    y2 = list_dataB

    fig, ax = plt.subplots(figsize = (20, 12))
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.title('LongShortAcc_close_'+day)

    ax2 = ax.twinx()
    ax.plot(x, y1, color = 'g')
    ax2.plot(x, y2, color = 'b')

    ax.set_ylabel('LongShortAcc', color = 'g')
    ax2.set_ylabel('close', color = 'b')

    plt.savefig('OUTPUT/LongShortAcc_close_'+day+'.png')

if __name__ == '__main__':
    chart(day='6h',linit=50)