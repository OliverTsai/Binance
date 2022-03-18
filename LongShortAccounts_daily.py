import LongShortAccounts_yesterday as longShortAccounts_yesterday

def run():
    longShortAccounts_yesterday.get_top_long_short_new(period='5m',limit=500,filename="CSV/LongShortAccounts_5m.csv")
    longShortAccounts_yesterday.get_top_long_short_new(period='30m',limit=500,filename="CSV/LongShortAccounts_30m.csv")
    longShortAccounts_yesterday.get_top_long_short_new(period='1h',limit=500,filename="CSV/LongShortAccounts_1h.csv")
    longShortAccounts_yesterday.get_top_long_short_new(period='4h',limit=500,filename="CSV/LongShortAccounts_4h.csv")
    longShortAccounts_yesterday.get_top_long_short_new(period='6h',limit=500,filename="CSV/LongShortAccounts_6h.csv")
    longShortAccounts_yesterday.get_top_long_short_new(period='1d',limit=500,filename="CSV/LongShortAccounts_1d.csv")