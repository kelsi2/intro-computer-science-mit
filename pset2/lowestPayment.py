balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentRate = 0
initialBalance = balance

while balance > 0:
  for i in range(12):
    balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
  if balance > 0:
    monthlyPaymentRate += 10
    balance = initialBalance
  elif balance <= 0:
    break

print('Lowest payment: ', monthlyPaymentRate)