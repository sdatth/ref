## Datatypes
# Integer
this_is_integer = 111_222_333
this_is_same = 111222333
print (this_is_integer)
print (this_is_same)

# Float
this_is_float = 12.444
this_is_also_float = 111_222_3334.3434
print (this_is_float)
print (this_is_also_float)

# String
this_is_string = "Dani"
print (this_is_string)                         # prints 'Dani'
print (this_is_string[0])                      # prints 'D'
print (this_is_string[1] + this_is_string[3])  # prints 'ai'

# Boolean (Note the first letter should be capital)
var1 = True
var2 = False

# type function to check the data type
print (type(this_is_integer))     # <class 'int'>
print (type(this_is_float))       # <class 'float'>
print (type(this_is_string))      # <class 'str'>
print (type(var1))                # <class 'bool'>
print (type(len(this_is_string))) # <class 'int'>

# type conversion from int to str
name = input("What is your name ")
print ("Your name contains "  + str(len(name)) + " charactors" )

# from str to int
a = "123"
print ( 12 + int(a) )   # prints '135'

# from int to float
a = 123
print ( float(a) )      # prints '123.0'

# when two digit number is inputed to one variable add those two digits
two_digit_number = input( "Enter two digit number ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a+b)
 
# Maths in python
# priority is PEMDAS Parenthese () , Exponents ** , Multiplication * , Division / , Addition + , Substraction -

# BMI Calculator 
# BMI = Weight / Height^2 
bmi = int(weight) / ((float(height))**2)  

# Round function to round of a number

print ( round(8/3) )      # prints 3
print ( round(8/3,4) )  # prints 2.6667  - keeps 4 decimal points 

# Some numbers to round
valueA = 3.14159265359    # 3
valueB = 1845.7409947     # 1846 
valueC = -100.95          # -101 
valueD = 9.5432           # 10
valueE = 34.49953         # 34

# short notation
score = 0
score += 1
score -= 1
score *= 1
score /= 1

# f-string
score = 1
height = 2.1
isWinning = True
print ( f"Adam's height is {height} , score is {score} and your are winning is {isWinning}" )


# Project - Tip Calculator

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


