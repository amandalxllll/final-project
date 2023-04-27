import yfinance as yf

def get_tickers(tickers_symbols):
    """
    Get the ticker objects for a list of ticker symbols
    """
    tickers_symbols = tickers_symbols.split()
    tickers = yf.Tickers(tickers_symbols)
    return tickers

def get_current_prices(tickers_symbols):
    tickers = get_tickers(tickers_symbols)
    prices = []
    for ticker in tickers.tickers:
        prices.append(yf.Ticker(ticker).info['regularMarketOpen'])
    return prices

def stock_return(tickers_symbols, purchase_prices):
    """
    Calculate the returns on a list of stock investments
    """
    current_prices = get_current_prices(tickers_symbols)
    individual_returns = []
    for i, tickers_symbols in enumerate(tickers_symbols.split()):
        market_price = current_prices[i]
        stock_return = (market_price - purchase_prices[i]) / purchase_prices[i]
        individual_returns.append(stock_return)
    return individual_returns

def calculate_portfolio_percentages(tickers_symbols, amount_invested):
    """
    Given a list of ticker symbols and the amount invested in each symbol, returns the percentage
    of the total portfolio value that each symbol represents.
    """
    current_prices = get_current_prices(tickers_symbols)
    total_value = 0
    percentages = []


tickers_symbols = "AAPL MSFT"
purchase_prices = [140, 150]
amount_invested = [5,10]
current_prices = get_current_prices(tickers_symbols)
print("Length of current_prices:", len(current_prices))
print("Length of amount_invested:", len(amount_invested))