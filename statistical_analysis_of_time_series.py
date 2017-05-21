import pandas as pd
import matplotlib as plt
from trading_file_manipulation import *


# Computes the mean, median, and standard deviation for a dataframe containing stock data
def mean_median_standard_deviation():
    dates = pd.date_range('2013-01-01', '2015-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    ### Compute global statistics for each stock
    # Prints the mean for each stock symbol for the entire dataframe
    print("Mean:\n", df.mean())
    # Prints the median for each stock symbol for the entire dataframe
    print("Median:\n", df.median())
    # Prints the standard deviation for each stock symbol for the entire dataframe
    print("Standard Deviation:\n", df.std())


### Rolling calculations are done on a set window.
# Eg. A 20 day window states that the mean is calculated for a 20 day period where the window is moved up
# one day for every other subsequent calculation until the last date.
def get_rolling_mean(df_object, window):
    return df_object.rolling(window).mean()


def get_rolling_std(df_object, window):
    return df_object.rolling(window).std()


# Bollinger Bands consists of two bands. The upper band is:  (rolling mean + (2 * standard deviation))
# The lower band is: (rolling mean - (2 * standard deviation)).
def get_bollinger_bands(rm, rstd):
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


def rolling_statistics():
    dates = pd.date_range('2013-01-01', '2015-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    ### Compute rolling mean using 20 day window; rm stands for rolling mean
    # Below is a deprecated method for computing rolling mean
    rm_SPY_deprecated = pd.rolling_mean(df['SPY'], window=30)

    # Current method of computing rolling mean
    rm_SPY_current = df['SPY'].rolling(20).mean()

    # Add rolling mean to same plot
    rm_SPY_current.plot(label='Rolling Mean 20 days window', ax=ax)
    rm_SPY_deprecated.plot(label='Rolling Mean 30 days window', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def bollinger_bands():

    dates = pd.date_range('2013-01-01', '2013-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    ### Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


# Compute and return the daily return values
def compute_daily_returns(df_object):
    ### Copy given DataFrame to match size and column names
    # daily_returns_df = df_object.copy()

    ### Compute daily returns for row 1 onwards
    # daily_returns_df[1:] = (df_object[1:] / df_object[:-1].values) - 1

    # Using Pandas to compute daily returns for row 1 onwards
    # df_object is the standard dataframe and df_object.shift(1) is the dataframe with all
    # indexes increased by 1 and the index 0 is initialised to NaN.
    # Therefore, the value of the index 1 is shifted into index 2 and so forth.
    # Dataframe division divides each index in dataframe A by its respective index in dataframe B.
    # T = Today; The formula for daily returns is ((price[T] / price[T - 1]) -1)
    # When we shift the dataframe by 1. We are aligning T to be divided by T - 1.
    daily_returns_df = (df_object / df_object.shift(1)) - 1

    # Set daily returns for row 0 to 0
    daily_returns_df.ix[0, :] = 0

    return daily_returns_df


def daily_returns_function():
    # One month only
    dates = pd.date_range('2015-07-01', '2015-07-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


# Calculates cumulative returns for a dataframe
def compute_cumulative_returns(df_object):
    # Cumulative returns formula
    # T = Today
    # cumulative_return[T] = ((price[T] / price[0]) - 1)

    # Divides each index by the first index for its respective symbol

    cumulative_return_cal = (df_object / df_object.ix[0, :]) - 1
    return cumulative_return_cal


# Calculates cumulative returns for symbols for a specific date range
def cumulative_returns_function():
    dates = pd.date_range('2016-12-01', '2016-12-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    cumulative_returns = compute_cumulative_returns(df)
    plot_data(cumulative_returns, title="Cumulative Returns", ylabel="Cumulative Return")

if __name__ == "__main__":
    # mean_median_standard_deviation()
    # rolling_statistics()
    # bollinger_bands()
    # daily_returns_function()
    cumulative_returns_function()
