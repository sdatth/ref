import random

random_integer = random.randint(10 , 100)   # prints a random number between 10 to 100 including 10 & 100
random_float = random.random()              # prints a number between 0.1 to 0.99999999....

print (random_integer)
print (random_float)


# lists
states = ["KAR","HYD","DEL","KER"]

# printing
print(states)
print(states[0])                                  # print first state
print(states[-1])                                 # print last state
print(states[0][1])                               # print second letter of first state

# modification
states[2] = "KOL"                                 # change the value at a certain index
states.append("GUJ")                              # append to the end of the list
states.extend(["state-a","state-b","state-c"])    # extends the list with new ones inputted
print(states) 

# nested list
list1 = [1,2,3,4]
list2 = ["item1","item2","item3"]
combined_list = [list1,list2]
print(combined_list)

# find index of a particular element
letter = input().lower()
letter_list = ["a", "b", "c"]
letter_index = letter_list.index(letter)
print(letter_index)

# random person will pay for the bill program
import random
names = ["name1","name2","name3"]
name_len = len(names) - 1
random_int = random.randint(0, name_len)
print(f"{names[random_int]} is going to buy the meal today!")


# rock paper scissor game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Enter your choice: ").lower()
game_list = ["rock","paper","scissors"]
game_image = [rock,paper,scissors]
rand_index_num = random.randint(0,2)
program_choice = game_list[rand_index_num]
program_image = game_image[rand_index_num]

user_index = game_list.index(user_choice)
user_image = game_image[user_index]


print(f"\nUser's choice is\n {user_image}")
print(f"Program's choice is\n {program_image}\n")

if user_choice == "rock":
    if program_choice == "rock":
        print("Draw")
    elif program_choice == "paper":
        print("You Loose")
    elif program_choice == "scissors":
        print("You Win")        

elif user_choice == "paper":
    if program_choice == "paper":
        print("Draw")
    elif program_choice == "scissors":
        print("You Loose")
    elif program_choice == "rock":
        print("You Win")

elif user_choice == "scissors":
    if program_choice == "scissors":
        print("Draw")
    elif program_choice == "rock":
        print("You Loose")
    elif program_choice == "paper":
        print("You Win")        


# instructors logic

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
