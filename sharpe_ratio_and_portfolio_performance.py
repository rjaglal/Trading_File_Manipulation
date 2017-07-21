import numpy as np
import pandas as pd
import matplotlib as plt
from trading_file_manipulation import *
import scipy.optimize as spo


def allocations_df_function(norm_df, allocation_list):

    num_of_columns_in_df = norm_df.shape[1]
    number_of_allocations = len(allocation_list)

    if num_of_columns_in_df == number_of_allocations:
        alloc_df = norm_df * allocation_list
        return alloc_df
    else:
        print("ERROR: The number of allocations " +
              str(number_of_allocations) +
              " do not match number of stocks " +
              str(num_of_columns_in_df))
        return


def initialize_portfolio():
    start_date = '2013-01-01'
    end_date = '2016-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    allocations = [0.4, 0.4, 0.1]
    # start_val in lesson
    investment = 1000000


    # Stock Prices Dataframe
    df = get_data(symbols, dates)
    #print(df)
    #plot_data(df)

    # Normalized Prices dataframe to the first row of the dataframe
    normed_df = normalize_dataframe(df)
    #print(normed_df)
    #plot_data(normed_df)

    allocations_df_function(normed_df, allocations)


if __name__ == "__main__":
    initialize_portfolio()
