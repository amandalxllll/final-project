import yfinance as yf
#从ticker变成tickers需要多加s在所有的ticker上面
def get_ticker(ticker_symbol):
    """
    users can imput tickers 
    """
    ticker = yf.Ticker(ticker_symbol)
    return ticker

def get_current_price(ticker):
    market_price = ticker.info['regularMarketOpen']
    return market_price

def stock_return(ticker,purchase_price):

    market_price = ticker.info['regularMarketOpen']
    stock_return = (market_price - purchase_price)/purchase_price
    return stock_return

tickers = get_ticker("AAPL")
purchase_price = 140
current_price = get_current_price(tickers)
return_on_investment = stock_return(tickers, purchase_price)

print("Current price:", current_price)
print("Return on investment:", return_on_investment)