from trading_file_manipulation import *
import matplotlib as plt
import pandas as pd


# Fills in missing gaps in stock prices for all symbols in a
# dataframe.
def fill_in_missing_data():
    dates = pd.date_range('2012-01-01', '2017-05-7')
    symbols = ['SPY', 'AAPL']
    df = get_data(symbols, dates)
    plot_data(df)

    # Forward Fills the data and saves it in current dataframe
    df.fillna(method="ffill", inplace=True)

    plot_data(df)

    # Back Fills the data and saves it in current dataframe
    df.fillna(method="bfill", inplace=True)

    plot_data(df)

if __name__ == "__main__":
    fill_in_missing_data()
