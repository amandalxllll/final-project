"""
A website using Flask which prompt user to enter
stocks they hold, time they purchase, price/share they purchase,
and the number of unit they purchased for each of the stock.
.
"""

from flask import Flask, request, render_template
from returnportfolio import get_portfolio_return

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index2.html')

@app.route('/', methods=['GET', 'POST'])
def portfolio_return():
    if request.method == 'POST':
        # print('post')
        try:
            # print(request.form.get('tickers_symbols'))
            tickers_symbols = request.form.get('tickers_symbols').split()
            purchase_prices = request.form.get('purchase_prices').split()
            amount_invested = request.form.get('amount_invested').split()
            purchase_prices = list(map(int, purchase_prices))
            amount_invested = list(map(int, amount_invested))
            print(tickers_symbols, purchase_prices, amount_invested)
            result = get_portfolio_return(tickers_symbols, purchase_prices, amount_invested)
            print(result)
            return render_template('returnportfolio.html', result=result)
        except Exception as e:
            print(e)
            return render_template('error.html') 
    else:
        return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)

