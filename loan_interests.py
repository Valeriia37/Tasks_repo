
print('This is a calculator for calculating the interest paid on a loan.\nPlease insert following information^')
try:
    S = abs(int(input('Loan: ')))
    r = abs(int(input('Interest rate (if 12%, then type 12): ')))
    n = abs(int(input('Loan term (in months): ')))
    k = abs(int(input(f'For what period do you want to calculate the interest paid on the loan? '
                      f'Insert number from 1 to {n}: ')))
    if k > n:
        print(f'Incorrect period. It must be in the range from 1 to {n}')
        raise ValueError
except ValueError:
    print('\nYou have entered an invalid value. Please restart the program.')

# monthly interest rate
p = r/100/12
s = S
print(f'\nCumulative interest paid on a loan for {k} months out of {n} months:')
# The simple interest method
print(f'The simple interest method: {round(s * p * k, 2)}')

# The normal loan amortization method
# the amount of the annuity monthly payment
x = round(S * (p + p / ((1 + p) ** n - 1)))
s = S
interest_paid_sum = 0
for i in range(1, k + 1):
    interest_paid = round(s * p, 2)
    interest_paid_sum += interest_paid
    s = s - (x - interest_paid)
print(f'The normal loan amortization method: {round(interest_paid_sum, 2)}')

# The fixed principal amortization method
# principal
s = S
b = round(s / n, 1)
interest_paid_sum = 0
for i in range(1, k + 1):
    interest_paid = round(s * p, 2)
    interest_paid_sum += interest_paid
    s = s - b
print(f'The fixed principal amortization method: {round(interest_paid_sum, 2)}')

