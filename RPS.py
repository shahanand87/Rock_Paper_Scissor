#This program is rocks paper scicssors

from random import randint
from time import sleep

options = ["R", "P", "S"]
loser = "You Lost!"
winner = "You Win!"

def decide_winner(user_choice, computer_choice):
  print "You selected %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  user_choice_index = option.index(user_choice)
  computer_choice_index = option.index(computer_choice)
  if user_choice == computer_choice:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print winner
  elif user_choice_index == 1 and computer_choice_index == 0:
    print winner
  elif user_choice_index == 2 and computer_choice_index == 1:
    print winner
  elif user_choice_index > 2:
    return
  else:
  	print loser
    
def play_RPS():
  print "Rocks, Paper, Scissor, Shoot!"
  user_choices = raw_input("Please select R for Rock, P for Paper, or S for Scissors: ")
  user_choices = userchoice.upper()
  computer_choices = options[randint(0,(len(options)-1))]
  decide_winner(user_choices, computer_choices)

play_RPS()  
  
