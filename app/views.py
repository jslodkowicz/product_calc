from flask import render_template, request

from app import app
from app.forms import CalcForm
from app.product_mvp import price_calc


@app.route("/", methods=["GET", "POST"])
def index():
    form = CalcForm()
    if request.method == "POST" and form.validate():
        quantity = form.quantity.data
        price = form.price.data
        state = form.state.data
        res = price_calc(quantity, price, state)
    else:
        res = None
    return render_template("index.html", form=form, res=res)
