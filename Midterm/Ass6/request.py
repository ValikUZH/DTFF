import requests
import time
import datetime


def readCryptoSince(s,market):
    unixtime = str(int(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())))
    tick_interval = '1h'
    url = 'https://api.binance.com/api/v3/klines?symbol=' + market + '&interval=' + tick_interval + "&limit=75&startTime=" + unixtime
    return requests.get(url).json();


s = "15/06/2021"
market = 'BTCUSDT'

result = readCryptoSince(s,market)
print(result)