import Candlestick_yesterday as candlestick_yesterday


def run():
    candlestick_yesterday.get_candlestick_new(interval="5m", limit=500,filename="CSV/Candlestick_5m.csv")
    candlestick_yesterday.get_candlestick_new(interval="30m", limit=500,filename="CSV/Candlestick_30m.csv")
    candlestick_yesterday.get_candlestick_new(interval="1h", limit=500,filename="CSV/Candlestick_1h.csv")
    candlestick_yesterday.get_candlestick_new(interval="4h", limit=500,filename="CSV/Candlestick_4h.csv")
    candlestick_yesterday.get_candlestick_new(interval="6h", limit=500,filename="CSV/Candlestick_6h.csv")
    candlestick_yesterday.get_candlestick_new(interval="1d", limit=500,filename="CSV/Candlestick_1d.csv")
