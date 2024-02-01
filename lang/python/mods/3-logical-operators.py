print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

## Simple If 
# Greater than
if height > 120:
    print("You can ride")
else:
    print("You cannot ride")

''' More operators
 <     # less than
 <=    # less than or equal to
 >     # greater than
 =    # Greater than or equal to
 ==    # Equal to
 !=    # Not Equal to
'''

# Nested If
# Python program to demonstrate 
# nested if statement 
  
num = 15
if num >= 0: 
    if num == 0: 
        print("Zero") 
    else: 
        print("Positive number") 
else: 
    print("Negative number") 


# Elif
number = 0
if number > 0:
    print('Positive number')
elif number <0:
    print('Negative number')
else:
    print('Zero')

print('This statement is always executed')


# Multiple If example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


# love score game
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

concat_name = name1.lower() + name2.lower()
d1 = 0
d2 = 0 
# Iterate over the string
for element in concat_name:
    if element == "t" or element == "r" or element == "u" or element == "e":
        d1 += 1

    if element == "l" or element == "o" or element == "v" or element == "e":
        d2 += 1

score = int(str(d1) + str(d2))

if score <= 10 or score >= 90:
    print (f"Your score is {score}, you go together like coke and mentos.")

elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.") 



## Tresure game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")