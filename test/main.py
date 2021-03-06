import pandas as pd
import numpy as np
from quantsc.core import TimeSeries
from quantsc import data
import quantsc as qsc


# from data.__random import seasonal


# from core2 import stock

def get_random_series(size,method='series'):
    dates = list(pd.date_range(start="4/2/2022", end="4/4/2022", periods=size))
    data = np.random.normal(size=size)
    if method == 'series':
        series_data = pd.Series(data=data, index=dates)
    elif method == 'numpy':
        series_data = np.array(np.array([dates,data]).T)
    return TimeSeries(series_data)

def get_dataframe(size, method='dataframe'):
    dates = list(pd.date_range(start="10/20/2003", end="10/20/2013", periods = size))
    #data = list()
    df = pd.DataFrame({"values" : [2, 2, 2],"PE" : [1, 2, 3], "earnings" : [213, 223, 32], "income" : [112, 23, 35], "dividends" : [11, 23, 32]})
    df.index = list(pd.date_range(start="4/4/2021",end="4/5/2021",periods=3))
    #print(df)
    return df

# def get_seasonal_series():


def test_to_string():
    df = get_dataframe(0)
    ts = TimeSeries(df)
    # print(ts.to_string(indicators=False))
    # print(ts.to_string(indicators=True))
    print(ts.to_string(indicators=['PE','income']))
    data.random


if __name__ == "__main__":
    # print(get_random_series(10,method='numpy'))
    # print(get_dataframe(3, method='dataframe'))
    # df = get_dataframe(0)
    # ts = TimeSeries(df)
    # test_to_string()
    # ts = TimeSeries()
    # print(data.any_func())
    # data.generate_random(1)
    # data.random.seasonal()

   #---------------Test 1: Initialization---------#

    ts = TimeSeries()
    print(ts)