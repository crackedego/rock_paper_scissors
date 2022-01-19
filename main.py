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
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
outcomes = [rock, paper, scissors]

if player_choice >= 3 or player_choice < 0:
  print("One of the players is bonkers! Play Again!!")
else:
  comp_result = outcomes[comp_choice]
  player_result = outcomes[player_choice]


  if comp_choice == player_choice:
    print(player_result)
    print("Computer chose:")
    print(comp_result)
    print("Draw")
  elif comp_choice == 0:
    if player_choice == 1:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("You Win")
    else:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("You Lose")
  elif comp_choice == 1:
    if player_choice == 2:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("Tou Win")
    else:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("You Lose")
  elif comp_choice == 2:
    if player_choice == 0:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("You Win")
    else:
      print(player_result)
      print("Computer chose:")
      print(comp_result)
      print("You Lose")             

