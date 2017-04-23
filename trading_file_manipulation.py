import pandas as pd
import matplotlib.pyplot as plt


def read_csv():
    df = pd.read_csv("data_files/comtrade.csv")
    print(df[['Reporter', 'Trade Value (US$)']][100:131])
    df[['Reporter', 'Trade Value (US$)']][100:131].plot()
    plt.show()


def hello_world():
    print("Hello World")

if __name__ == "__main__":
    hello_world()
    read_csv()
