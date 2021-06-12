from flask import render_template

def display_value(target_value,value_today,invest_amount,investment):
    difference=value_today-target_value
    if target_value==value_today:
            return render_template('result.html',invest_amount=invest_amount,target_value=target_value,value_today=value_today,monthly_investment=investment,difference=difference)
    elif target_value > value_today:
            return render_template('result.html',invest_amount=invest_amount,target_value=target_value,value_today=value_today,monthly_investment=investment,difference=difference)    
    elif target_value < value_today:
            return render_template('result.html',invest_amount=invest_amount,target_value=target_value,value_today=value_today,monthly_investment=investment,difference=difference)    


        