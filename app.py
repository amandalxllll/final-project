"""
A website using Flask which prompt user to enter
stocks they hold, time they purchase, price/share they purchase,
and the number of unit they purchased for each of the stock.
.
"""

from flask import Flask, request, render_template
from returnportfolio import get_portfolio_return

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def portfolio():
    if request.method == 'POST':
        tickers_symbols = request.form['tickers_symbols']
        purchase_prices = request.form['purchase_prices']
        amount_invested = request.form['amount_invested']
        try:
            portfolio_return = get_portfolio_return(tickers_symbols, purchase_prices, amount_invested)
            return render_template('returnportfolio.html', portfolio_return=portfolio_return)
        except Exception as e:
            print("error")
            return render_template('error.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)