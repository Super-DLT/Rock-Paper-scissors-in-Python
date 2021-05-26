# import random library
import rand
# The basic data
rock = "👊"
paper = "✋"
scissors= "🖖"
# Say Hello to user
print("Welcome to the Game:)")
# Get user choice 
user = int(input("enter  1  for rock,  2  for paper,  3  for scissors :\n"))
# Get Computer choice by random
computer = int(rand.random_range(1,3))
# better data set for handle data
game = [rock,paper,scissors]
# Check conditions do magic
if user == computer :
    print(f"User : {game[user -1]}\nComputer: {game[computer -1]}\nEqual")
elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print(f"User : {game[user -1]}\nComputer: {game[computer -1]}\nYou are The Winner")
else :
    print(f"User : {game[user -1]}\nComputer: {game[computer -1]}\nComputer are The Winner")      