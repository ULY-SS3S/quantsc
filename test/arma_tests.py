from quantsc.core import Stock


def generate_stationary():
    apple_stock = Stock("AAPL")
    #print(apple_stock.get_data())
    dividends = apple_stock.dividends()
    earnings = apple_stock.earnings()
    print(dividends, earnings)
    #print(apple_stock.get_earnings("APPL"))
    #tsApple = TimeSeries(apple_stock.get_data())
    #tsApple.plot()

    #tsApple.take_diff(3)
    #tsApple.take_autocorrelation(3)
    #tsApple.take_partial_autocorrelation(1)
    #tsApple.model_arima(1, 1, 2)


if __name__ == "__main__":
    generate_stationary()



