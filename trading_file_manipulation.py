import pandas as pd
import matplotlib.pyplot as plt
import os


# Example function for plotting and prints a dataframe with
# standard index 0..n
def read_csv():
    df = pd.read_csv("data_files/comtrade.csv")
    print(df[['Reporter', 'Trade Value (US$)']][100:131])
    df[['Reporter', 'Trade Value (US$)']][100:131].plot()
    plt.show()


# Returns CSV file path for given ticker symbol
def symbol_to_path(symbol, base_dir="data_files"):
    return os.path.join(base_dir, "{}_data.csv".format(str(symbol)))


# Plot stock price dataframes
def plot_data(df, title="Stock Prices", xlabel="Date", ylabel="Price"):
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


# Pulls in all stock csv files into one dataframe
# and sets 'SPY' as the main stock in dataframe
def get_data(symbols_var, dates):
    # Creates a new dataframe with dates as the index
    df = pd.DataFrame(index=dates)

    ### IMPORTANT: The insert statment places the element
    ### into the memory location of the variable.
    ### Therefore the value of the variable is even changed outside of
    ### the function
    if 'SPY' not in symbols_var:
        symbols_var.insert(0, 'SPY')

    # index_col --> Use Date as the Index column
    # parse_dates --> Turn date into datetime object
    # usecols --> Only read in these columns
    # na_values --> Takes the string nan into type Nan
    for symbol in symbols_var:
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col="Date",
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        # Renames the requested column to a unique value
        # so clashing will not occur when when multiple stocks
        # are joined
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # Left join df_temp to df
        df = df.join(df_temp)

        # Removes all NaN from the SPY stock data set
        # SPY is used as the main stock to compare others with
        # in this example
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])

    return df


# Plots a dataframe for specific columns and period
def plot_selected(df, columns, start_index, end_index):

    #           string      string     list
    df = df.ix[start_index:end_index, columns]
    plot_data(df, title="Slices Stock Price")


# Normalizes all stock in dataframe
def normalize_dataframe(df):
    return df / df.ix[0, :]


def stock_engine():
    start_date = '2012-01-01'
    end_date = '2017-05-06'
    dates = pd.date_range(start_date, end_date)

    # List of stock symbols
    symbols = ['GOOG', 'IBM', 'GLD']

    df = get_data(symbols, dates)

    slice_start_date = '2012-05-06'
    slice_end_date = '2017-05-06'

    norm_df = normalize_dataframe(df)
    selective_symbols = ['GOOG', 'IBM']

    ### IMPORTANT: The symbols variable below is affected
    ### by an insert statment in another fuction add SPY to
    ### the symbols list via input into direct memory location
    plot_selected(norm_df, symbols, slice_start_date, slice_end_date)


def hello_world():
    print("Hello World")

if __name__ == "__main__":
    stock_engine()
