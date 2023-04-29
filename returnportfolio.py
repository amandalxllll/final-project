from turtle import pd
import yfinance as yf
import numpy as np


def get_tickers(tickers_symbols):
    """
    Get the ticker objects for a list of ticker symbols
    """
    # tickers_symbols = tickers_symbols.split()
    tickers = yf.Tickers(tickers_symbols)
    return tickers


def get_current_prices(tickers_symbols):
    tickers = get_tickers(tickers_symbols)
    # print(tickers.tickers)
    prices = []
    for ticker in tickers.tickers:
        price = yf.Ticker(ticker).info["regularMarketOpen"]
        # print(price)
        prices.append(price)
    # print(prices)
    return prices


def stock_return(tickers_symbols, purchase_prices):
    """
    Calculate the returns on a list of stock investments
    """
    current_prices = get_current_prices(tickers_symbols)
    individual_returns = []
    for i, tickers_symbols in enumerate(tickers_symbols):
        market_price = current_prices[i]
        stock_return = (market_price - purchase_prices[i]) / purchase_prices[i]
        individual_returns.append(stock_return)
    return individual_returns


def calculate_portfolio_percentages(tickers_symbols, amount_invested):
    """
    Given a list of ticker symbols and the amount invested in each symbol, returns the percentage
    of the total portfolio value that each symbol represents.
    """
    # tickers_symbols_list = tickers_symbols.split()
    current_prices = get_current_prices(tickers_symbols)
    # print(current_prices)
    total_value = 0
    percentages = []
    for i in range(len(tickers_symbols)):
        value = current_prices[i] * amount_invested[i]
        total_value += value
    for i in range(len(tickers_symbols)):
        percentage = 100 * current_prices[i] * amount_invested[i] / total_value
        percentages.append(percentage)
    # print(percentages)
    return percentages


def get_portfolio_return(tickers_symbols,purchase_prices, amount_invested):
    percentage = calculate_portfolio_percentages(tickers_symbols, amount_invested)
    # print(percentage)
    individual_return = stock_return(tickers_symbols, purchase_prices)
    # print(individual_return)
    portfolio_return = np.dot(individual_return,percentage)
    return portfolio_return

def main():
    """
    You can test the functions here
    """
    tickers_symbols = ["AAPL", "MSFT"]
    purchase_prices = [140, 150]
    amount_invested = [1000, 2000]
    # current_prices = get_current_prices(tickers_symbols)
    # returns_on_investment = stock_return(tickers_symbols, purchase_prices)
    # stock_percentage = calculate_portfolio_percentages(tickers_symbols, amount_invested)
    portfolio_return = get_portfolio_return(tickers_symbols, purchase_prices, amount_invested)
    # print(current_prices)
    # print(returns_on_investment)
    # print(stock_percentage)
    print(portfolio_return)

if __name__ == "__main__":
    main()
