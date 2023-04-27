"""
A website using Flask which prompt user to enter
stocks they hold, time they purchase, price/share they purchase,
and the number of unit they purchased for each of the stock.
return the corresponding Portfolio Return for the past week in a table.
"""

from flask import Flask, request, render_template
import pandas as pd
from returnportfolio import get_portfolio_return
import json

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def portfolio_return():
    if request.method == 'POST':
        try:
            tickers_symbols = request.form['tickers_symbols']
            purchase_prices = request.form["purchase_prices"]
            amount_invested = request.form["amount_invested"]
            result = get_portfolio_return(tickers_symbols,purchase_prices, amount_invested)


        except Exception:
            return render_template("error.html")