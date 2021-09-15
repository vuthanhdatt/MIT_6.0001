annual_salary = int(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save:'))
total_cost = int(input('Enter the cost of your house:'))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal:'))

portion_down_payment = .25
current_savings = 0
r = .04
time = 0

cost = total_cost*portion_down_payment
salary = annual_salary/12
savings = salary*portion_saved
r_month = r/12

while current_savings < cost:
    current_savings += savings + current_savings*r_month
    time +=1
    if time%6 == 0:
        salary += salary*semi_annual_raise
        savings = salary*portion_saved
print(f'Number of months: {time}')