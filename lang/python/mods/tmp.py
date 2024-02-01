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


