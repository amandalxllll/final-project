import yfinance as yf

tickers = yf.Tickers('msft aapl')

# access each ticker using (example)
info = tickers.tickers['MSFT'].info
history = tickers.tickers['AAPL'].history(period="1mo")

print(history)
