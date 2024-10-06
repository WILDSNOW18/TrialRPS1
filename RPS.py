import random


compsChoice = ""

compsNum = random.randint(1,3)

if compsChoice == 1:
    compsChoice = "Rock"
    
elif compsNum == 2:
    compsChoice = "Paper"

else:
    compsChoice = "Scissors"

#Added the users ability to choose
userChoice = input("What would you like: Rock, Paper, or Scissors")

if userChoice == compsChoice:
    print("Tie")

#Added if the computer or the player chooses rock
if userChoice == "Rock" and compsChoice == "Paper":
    print("Loose")
if userChoice == "Rock" and compsChoice == "Scissors":
    print("Win")
    
if userChoice == "Scissors" and compsChoice == "Paper":
    print("Win")
if userchoice == "Scissors" and compsChoice == "Rock":
    print("Loose")

#Added if the computer or the player chooses Paper

if userChoice == "Paper" and compsChoice == "Rock":
    print("Win")
if userChoice == "Paper" and compsChoice == "Scissors":
    print("Loose")
