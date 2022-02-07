balance = 999999
annualInterestRate = 0.18

initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
lowerBound = initBalance/12.0
upperBound = (initBalance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upperBound + lowerBound)/2
    balance = initBalance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lowerBound = monthlyPaymentRate
    elif balance < -epsilon:
        upperBound = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))