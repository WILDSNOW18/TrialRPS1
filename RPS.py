import random


compsChoice = ""

compsNum = random.randint(1,3)

if compsChoice == 1:
    compsChoice = "Rock"
    
elif compsNum == 2:
    compsChoice = "Paper"

else:
    compsChoice = "Siccors"

#Added the users ability to choose
userChoice = input("What would you like: Rock, Paper, or Scissor")
