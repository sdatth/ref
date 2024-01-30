#If the bill was $150.00, split between 5 people, with 12% tip. 
#Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)                  ## this doesn't round to 2 if there are no decimal present
print(f"Each person should pay: {bill_per_person:.2f}")   ## it needs formating not round function