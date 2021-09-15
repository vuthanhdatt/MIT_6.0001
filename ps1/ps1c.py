annual_salary = int(input('Enter your annual salary:'))

portion_saved_high = 1
portion_saved_low = 0
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = .25
current_savings = 0
r = .04
time = 36
e = 100
step = 0

portion_saved = (portion_saved_high + portion_saved_low)/2
cost = total_cost*portion_down_payment
salary = annual_salary/12
savings = salary*1
r_month = r/12

for i in range(1,37,1):
        current_savings += savings + current_savings*r_month
        if i%6 == 0:
            salary += salary*semi_annual_raise
            savings = salary*1
if current_savings < cost:
    print('It is not possible to pay the down payment in three years')
else:
    while abs(current_savings - cost) >= 1: 
        step +=1
        savings = 0
        current_savings = 0
        salary = annual_salary/12
        savings = salary*portion_saved
        for i in range(1,37,1):
            current_savings += savings + current_savings*r_month
            if i%6 == 0:
                salary += salary*semi_annual_raise
                savings = salary*portion_saved
        if current_savings < cost:
            portion_saved_low = portion_saved
        else:
            portion_saved_high = portion_saved
        portion_saved = (portion_saved_high + portion_saved_low)/2
    print(f'Best saving rate: {portion_saved}')
    print(f'Step in bisection search: {step}')
    

