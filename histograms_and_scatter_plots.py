import pandas as pd
import matplotlib as plt
from trading_file_manipulation import *
from statistical_analysis_of_time_series import *
import numpy as np

# Slope of a scatter plot is where you have a stock daily return
# scatter plotted against the market(that is the SPY).

# Beta is another name for the slope of the daily return scatter plot graph
# Beta also mean the reactivity of the stock to the market.
# If Beta is 1 that mean the stock grows the same amount as the market
# So if the market increased by 1% the stock you are graphing will also
# increase by 1%. If Beta is 2 that means if the market grows by 1% the
# stock you are measuring will grow by 2%

# Alpha is the "y value" of where the slope cut the line x = 0
# If Alpha is positive that means the stock is doing better than the market
# If Alpha is negative that means the stock is doing worse than the market

# Slope != correlation. Correlation is measure between 0 and 1
# Correlation is the how tightly packed the scatter plots(dots) are to the slope
# If most of the dots are next to the slope then we can say the correlation
# is almost 1. If most the dots are spaced out from the slope then we can
# stay correlation is almost 0


def scatter_plots():
    # Read data
    dates = pd.date_range('2013-01-01', '2016-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # Scatter Plot of SPY vs XOM
    daily_returns.plot.scatter(x='SPY', y='XOM')
    # y = mx + c ; beta_XOM = m ; alpha_XOM = c
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'],
                                     daily_returns['XOM'],
                                     1)

    print("beta_XOM = ", beta_XOM)
    print("alpha_XOM = ", alpha_XOM)

    ### Below plot is x vs y; This is the plot for the best line that
    ### represent the dots in the scatter plot
    ### First part of tuple
    # x = daily_returns['SPY']
    ### Second part of tuple
    # y = mx + c
    # m = beta_XOM
    # c = alpha_XOM
    ### Third part of tuple type of line
    ### Forth parh of tuple is the color of the line
    plt.plot(daily_returns['SPY'],
             beta_XOM * daily_returns['SPY'] + alpha_XOM,
             '-',
             color='r')
    plt.show()

    # Scatter plot SPY vs GLD ### NOTES ABOVE
    daily_returns.plot.scatter(x='SPY', y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'],
                                     daily_returns['GLD'],
                                     1)

    print("beta_GLD = ", beta_GLD)
    print("alpha_GLD = ", alpha_GLD)

    plt.plot(daily_returns['SPY'],
             beta_GLD * daily_returns['SPY'] + alpha_GLD,
             '-',
             color='r')
    plt.show()

    # Calculate correlation coefficient of ['SPY', 'XOM', 'GLD']
    print(daily_returns.corr(method='pearson'))


def multiple_stock_histogram_analysis():
    dates = pd.date_range('2013-01-01', '2016-12-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    #plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    #plot_data(daily_returns, title="Daily Returns", ylabel="Daily returns")

    # Plot histogram directly from dataframe
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc='upper right')
    plt.show()

    ### OR XXX FIX

    daily_returns['SPY'].plot.hist(bins=20)
    daily_returns['XOM'].plot.hist(bins=20)
    plt.show()


def one_stock_histogram_analysis():
    dates = pd.date_range('2013-01-01', '2016-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily returns")

    # Mean of daily returns for SPY
    mean = daily_returns['SPY'].mean()
    print('Mean = ', mean)
    # Std deviation of SPY
    std_deviation = daily_returns['SPY'].std()
    print('Std Deviation= ', std_deviation)

    # Plot a histogram of daily returns
    daily_returns.hist(bins=20)
    # The mean value as a line on the graph
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    # The positive std deviation on the graph
    plt.axvline(std_deviation, color='r', linestyle='dashed', linewidth=2)
    # The negative std deviation on the graph
    plt.axvline(-std_deviation, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    # The Kurtosis value of the histogram
    # A positive kurtosis is the sign of fat tails
    # A negative kurtosis is the sign of skinny tails
    print('Kurtosis = \n', daily_returns.kurtosis())

if __name__ == "__main__":
    #one_stock_histogram_analysis()
    multiple_stock_histogram_analysis()
    #scatter_plots()
