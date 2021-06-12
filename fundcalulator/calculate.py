import math


def invest(target_value,value_today,monthly_investment):
    difference = target_value - value_today
    invest_amount = monthly_investment + difference
    return invest_amount

#this is technically sumofGP     
def current_value(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    total=math.ceil(total)
    target_value = total-a
    return target_value
    
   

