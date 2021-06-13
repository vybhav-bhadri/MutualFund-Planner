from fundcalulator import app
from flask import render_template, request 
from fundcalulator.calculate import current_value,invest
from fundcalulator.display import display_value
import math

    

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        investment = int(request.form.get('monthly_investment'))
        return_rate = int(request.form.get('expected_return'))
        no_months = int(request.form.get('no_months'))
        value_today = int(request.form.get('value_today'))

        return_rate=return_rate/12

        target_value = current_value(investment, no_months+1, 1+return_rate/100)
        target_value=math.floor(target_value)
        invest_amount = invest(target_value,value_today,investment)
        invest_amount = math.floor(invest_amount)

        return display_value(target_value,value_today,invest_amount,investment)
  
    return render_template("index.html",title="MutualFund Planner | Invest in Mutual Funds using VIP & SIP methods")

@app.route('/learn')
def about():
    return render_template('learn.html',title="Learn | what is VIP?")

