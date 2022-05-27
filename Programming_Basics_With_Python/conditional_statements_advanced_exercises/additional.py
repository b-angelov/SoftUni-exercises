#scrapper
import yfinance as f
import easygui

company = f.Ticker("TSLA")
stock_data = company.history(period="1mo")
#
# print(stock_data)
# print(company.info)
# hist = company.history(period="5d")

easygui.msgbox(f"{stock_data}", title="simple gui")