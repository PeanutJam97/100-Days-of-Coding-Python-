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

#Write your code below this line 👇
Userinput = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
Computerinput = random.randint(0, 2)

Userinputint = int(Userinput)

if Userinputint > 2:
  print("You can only choose a number between 0-2.")

if Userinputint == 0:
  print("You:")
  print(rock)
elif Userinputint == 1:
  print("You:")
  print(paper)
else:
  print("You:")
  print(scissors)

if Computerinput == 0:
  print("Computer:")
  print(rock)
elif Computerinput == 1:
  print("Computer:")
  print(paper)
else:
  print("Computer:")
  print(scissors)

if Userinputint == Computerinput:
  print("This is a draw!")
elif Userinputint == 0 and Computerinput == 1:
  print("Computer Wins!")
elif Userinputint == 1 and Computerinput == 2:
  print("Computer Wins!")
elif Userinputint == 0 and Computerinput == 2:
  print("You Win!")
else: 
  print("You Win!")
