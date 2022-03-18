import Chart_yesterday as chart_yesterday

def run():
    chart_yesterday.chart(day='1d',linit=50)
    chart_yesterday.chart(day='1h',linit=50)
    chart_yesterday.chart(day='4h',linit=50)
    chart_yesterday.chart(day='6h',linit=50)
    chart_yesterday.chart(day='5m',linit=50)
    chart_yesterday.chart(day='30m',linit=50)