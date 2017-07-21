import requests
import pprint
import json
import sys
import time
import os
import sqlite3


db_file = "C:/Users/ravi/Documents/sqlite_db/stock_data.db"
btce_ticker_columns = '(updated INTERGER PRIMARY KEY, ' \
                      'high REAL, ' \
                      'low REAL,' \
                      'avg REAL,' \
                      'vol REAL,' \
                      'vol_cur REAL,' \
                      'last REAL,' \
                      'buy REAL,' \
                      'sell REAL)'


def get_data():
    #r = requests.get('http://chart.finance.yahoo.com/table.csv?s=AMD&a=3&b=30&c=2016&d=3&e=30&f=2017&g=d&ignore=.csv')

    symbol_pair = 'ltc_usd'

    r = requests.get('https://btc-e.com/api/3/depth/%s?limit=5000' % symbol_pair)

    #pprint.pprint(r.json()['ltc_usd'], indent=4)

    #pprint.pprint(r.json()['ltc_usd']['bids'], indent=4)

    while 1:
        print("Symbol Pair: %s" % symbol_pair)
        r = requests.get('https://btc-e.com/api/3/depth/%s?limit=5000' % symbol_pair)
        print("------------BIDS-------------")
        for i in r.json()[symbol_pair]['bids']:
            if i[1] > 300 and i[0] >= 40:
                print(i)
        print("------------ASKS-------------")
        for i in r.json()[symbol_pair]['asks']:
            if i[1] > 300 and i[0] <= 50:
                print(i)
        print(r.status_code)
        time.sleep(5)
        os.system('cls')


def drop_table(db_name=db_file, drop_table_name=''):

    drop_table_conn = sqlite3.connect(db_name)
    drop_table_cursor = drop_table_conn.cursor()
    print('INFO: Dropping table {0}'.format(drop_table_name))
    drop_table_cursor.execute('''
    DROP TABLE {0}
    '''.format(drop_table_name))
    print('INFO: {0} table dropped'.format(drop_table_name))
    drop_table_conn.close()


def create_table(db_name=db_file, create_table_name=''):

    create_table_conn = sqlite3.connect(db_name)
    create_table_cursor = create_table_conn.cursor()
    print('INFO: Creating table {0}'.format(create_table_name))
    create_table_cursor.execute('''
    CREATE TABLE {0} 
    {1}
    '''.format(create_table_name, btce_ticker_columns))
    print('INFO: {0} table created'.format(create_table_name))
    create_table_conn.close()


def get_ticker_data_for_symbol(sym_name=''):

    api = 'https://btc-e.com/api/3/ticker/{0}'.format(sym_name)
    r = requests.get(api)

    print(r.json())


if __name__ == "__main__":
    get_data()
    #drop_table(drop_table_name='btc_ltc')
    #create_table(create_table_name='btc_ltc')

    #sym_pair = 'ltc_usd'
    #get_ticker_data_for_symbol(sym_pair)
    #print(sqlite3.sqlite_version_info)
