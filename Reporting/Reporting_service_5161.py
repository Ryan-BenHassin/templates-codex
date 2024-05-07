
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt

class Reporting:
 def __init__(self, api_key):
 self.api_key = api_key

 def get_stock_info(self, ticker):
 stock = yf.Ticker(ticker)
 info = stock.info
 return info

 def get_historical_data(self, ticker, start_date, end_date):
 stock = yf.download(ticker, start_date, end_date)
 return stock

 def visualize_stock(self, ticker, start_date, end_date):
 data = self.get_historical_data(ticker, start_date, end_date)
 plt.figure(figsize=(10,5))
 plt.plot(data['Close'])
 plt.title(f'{ticker} Stock Price')
 plt.xlabel('Date')
 plt.ylabel('Price')
 plt.show()

 def generate_report(self, ticker, start_date, end_date):
 info = self.get_stock_info(ticker)
 data = self.get_historical_data(ticker, start_date, end_date)
 self.visualize_stock(ticker, start_date, end_date)
 return info, data

# Example usage
reporting = Reporting('YOUR_API_KEY')
ticker = 'AAPL'
start_date = datetime.today() - timedelta(days=30)
end_date = datetime.today()
info, data = reporting.generate_report(ticker, start_date, end_date)
print(info)
print(data)

