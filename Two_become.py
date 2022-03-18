import pandas as pd

def merge_csv(left_csv, right_csv, left_on, right_on, outputFilename='CSV/output.csv'):
    result = pd.merge(pd.read_csv(left_csv), pd.read_csv(right_csv), left_on=left_on, right_on=right_on)
    result = result[1:len(result)]
    result.to_csv(outputFilename, mode='a',header=False,index=False)
    
if __name__ == '__main__':
    merge_csv(left_csv='CSV/Candlestick_5m.csv', right_csv='CSV/LongShortAccounts_5m.csv', left_on='openTime', right_on='timestamp',outputFilename='CSV/LongShortAcc_close_5m.csv')