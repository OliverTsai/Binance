from os import name
import Two_become as become


def run():
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_1d.csv',left_csv = 'CSV/Candlestick_1d.csv',outputFilename = 'CSV/LongShortAcc_close_1d.csv', left_on='openTime', right_on='timestamp')
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_1h.csv',left_csv = 'CSV/Candlestick_1h.csv',outputFilename = 'CSV/LongShortAcc_close_1h.csv', left_on='openTime', right_on='timestamp')
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_4h.csv',left_csv = 'CSV/Candlestick_4h.csv',outputFilename = 'CSV/LongShortAcc_close_4h.csv', left_on='openTime', right_on='timestamp')
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_6h.csv',left_csv = 'CSV/Candlestick_6h.csv',outputFilename = 'CSV/LongShortAcc_close_6h.csv', left_on='openTime', right_on='timestamp')
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_5m.csv',left_csv = 'CSV/Candlestick_5m.csv',outputFilename = 'CSV/LongShortAcc_close_5m.csv', left_on='openTime', right_on='timestamp')
    become.merge_csv(right_csv = 'CSV/LongShortAccounts_30m.csv',left_csv = 'CSV/Candlestick_30m.csv',outputFilename = 'CSV/LongShortAcc_close_30m.csv', left_on='openTime', right_on='timestamp')
