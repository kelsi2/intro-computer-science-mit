balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
  
for i in range(12):
  balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * monthlyInterestRate)

print('Remaining balance: ', round(balance, 2))