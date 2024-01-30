# everything between double quotes will be printed
print ("print('what to print')")

# Add new line by using \n
print ("Hello world\nHello world\n Hello world")
# Output - 
#Hello world
#Hello world
# Hello world

# String concatenation
print ("Hello" + " " + "Angela")  # will print out 'Hello Angela'
print ("Hello" + "Angela")        # Will print out 'HelloAngela'
print ('We need to use single quotes inorder to use double quotes inside print statement "+" ')

# https://thonny.org/ use this to see how code is executed at everystep

# Input function, this will print 'hello' and the user input
print ("Hello" + input("What is your name") ) 

# String length
print(len(input())) # short version
name = input("What is your name ")
print ("Your name contains "  + str(len(name)) + " charactors" )

# Naming variable rule
user_name = "dani"
# 1user = "dani1"  # number cannot start at the beginning of the variable but can at the end or middle  

# Project - Brand name generator
print ("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print ("Your band name could be " + street + " " + pet)

