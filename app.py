from flask import Flask, render_template, request
from returnportfolio import get_portfolio_return


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def stockreturn():
    if request.method == "POST":
        try:
            tickers_symbols = request.form.getlist("tickers_symbols")
            purchase_prices = request.form.getlist("purchase_prices")  # Update variable name
            amount_invested = request.form.getlist['amount_invested']
            result = get_portfolio_return(tickers_symbols, purchase_prices, amount_invested)
            return render_template('returnportfolio.html', result=result)
        except Exception:
            return render_template('error.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

