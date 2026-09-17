# Program 17: Calculate Simple Interest
# Formula: (Principle * Rate * Time) / 100
# User Inputs
principle = float(input()) # Loan amount
rate = float(input()) # rate of interest
time = float(input()) # repayment time
# Calculate Interest
si = (principle * rate * time) / 100
# print the result
print(si)