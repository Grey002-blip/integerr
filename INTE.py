# 1. Assign data to variables
principal = 172000
boe_rate = 2.25
margin_rate = 1.49
# 2. Calculate the total annual interest rate as a decimal
# (e.g., 3.74% becomes 0.0374)
total_annual_rate_decimal = (boe_rate + margin_rate) / 100
# 3. Compute the annual interest amount 
annual_interest = principal * total_annual_rate_decimal
# 4. Compute the monthly interest amount (as requested)
interest = annual_interest / 12 
# Output the result to check
print(f"Monthly interest: {interest}")