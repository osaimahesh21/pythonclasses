"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""

# # Method 1 - Hard coding Values
# borrowed_amount = 10_000 # Principal
# rate_of_interest = 8.3 /100   # %
# loan_duration = 10 # years

# Method 2 - Getting values in run-time
borrowed_amount = int(input("Enter Borrowed Amount:"))
rate_of_interest = float(input("Enter Rate of Interest :")) / 100
loan_duration = int(input("Enter loan duration (in years):"))



# A = P (1 + rt)
payable_amount  = borrowed_amount * (1 + rate_of_interest * loan_duration)
interest_amount = payable_amount - borrowed_amount

print("Principle          :", borrowed_amount)
print("Rate of Interest   :", rate_of_interest)
print("Loan Duration      :", loan_duration)
print("Interest amount    :", interest_amount)
print("total amount to pay:", payable_amount)



# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php



borrowed_amount = 1000  # initial amount borrowed
rate_of_interest = 0.05  # 5% annual interest rate
loan_duration = 5  # loan duration in years

# Calculate compound interest
total_payable_amount = compound_interest(borrowed_amount, rate_of_interest, loan_duration)

# Calculate the interest amount
interest_amount = total_payable_amount - borrowed_amount

# Display the results
print("Principle          :", borrowed_amount)
print("Rate of Interest   :", rate_of_interest)
print("Loan Duration      :", loan_duration)
print("Interest amount    :", interest_amount)
print("Total amount to pay:", total_payable_amount)
