import requests
import pprint
import json
import sys
import time
import os


def get_data():
    #r = requests.get('http://chart.finance.yahoo.com/table.csv?s=AMD&a=3&b=30&c=2016&d=3&e=30&f=2017&g=d&ignore=.csv')

    r = requests.get('https://btc-e.com/api/3/depth/ltc_usd?limit=5000')

    #pprint.pprint(r.json()['ltc_usd'], indent=4)

    #pprint.pprint(r.json()['ltc_usd']['bids'], indent=4)

    while 1:
        r = requests.get('https://btc-e.com/api/3/depth/ltc_usd?limit=5000')
        print("------------BIDS-------------")
        for i in r.json()['ltc_usd']['bids']:
            if i[1] > 500 and i[0] >= 19:
                print(i)
        print("------------ASKS-------------")
        for i in r.json()['ltc_usd']['asks']:
            if i[1] > 500 and i[0] <= 24:
                print(i)
        print(r.status_code)
        time.sleep(5)
        os.system('cls')


if __name__ == "__main__":
    get_data()