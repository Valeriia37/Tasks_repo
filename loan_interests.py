import json
import sys

print('This is a calculator for calculating the interest paid on a loan.')

with open("data.json") as file:
    dict = json.load(file)

try:
    k = abs(int(input(f'For what period do you want to calculate the interest paid on the loan? '
                      f'Insert number from 1 to {dict["load_term"]}: ')))
    if k > dict['load_term']:
        print(f'Incorrect period. It must be in the range from 1 to {dict["load_term"]}')
        raise ValueError
except ValueError:
    print('\nYou have entered an invalid value. Please restart the program.')
    sys.exit(-1)

# monthly interest rate
p = dict['rate']/100/12
s = dict['load']
print(f'\nCumulative interest paid on a loan for {k} months out of {dict["load_term"]} months:')

# The simple interest method
print(f'The simple interest method: {round(s * p * k, 2)}')

# The normal loan amortization method
# the amount of the annuity monthly payment
x = round(dict['load'] * (p + p / ((1 + p) ** dict['load_term'] - 1)))
interest_paid_sum = 0
for i in range(1, k + 1):
    interest_paid = round(s * p, 2)
    interest_paid_sum += interest_paid
    s = s - (x - interest_paid)
print(f'The normal loan amortization method: {round(interest_paid_sum, 2)}')

# The fixed principal amortization method
s = dict['load']
# principal
b = round(s / dict['load_term'], 1)
interest_paid_sum = 0
for i in range(1, k + 1):
    interest_paid = round(s * p, 2)
    interest_paid_sum += interest_paid
    s = s - b
print(f'The fixed principal amortization method: {round(interest_paid_sum, 2)}')

# The information about the method used can also be written in json, then the if condition would be used in the code
