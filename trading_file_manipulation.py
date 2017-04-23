import pandas as pd


def read_csv():
    df = pd.read_csv("data_files/comtrade.csv")
    print(df['Reporter'][10:21])


def hello_world():
    print("Hello World")

if __name__ == "__main__":
    hello_world()
    read_csv()