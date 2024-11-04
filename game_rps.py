# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import random
from enum import Enum
from turtle import title

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain:
  
  title = " Game: Rock, Paper, Scissors (RPS) ".upper()
  print(title.center(50, "" + ("=") + ""))
  print ('')
  print("Welcome to the game of Rock, Paper, Scissors (RPS)!")

    
  print("")
  # Top Section of the Menu
  line01 = "*************************************************************"
  line02 = "*                                                           *"
  line03 = "* Enter...                                                  *"
  line04 = "* 1 for Rock,                                               *"
  line05 = "* 2 for Paper, or                                           *"
  line06 = "* 3 for scissors                                            *"
  line07 = "*                                                           *"
  # Bottom Section of the Menu
  line08 = "* Would you like to play again?                             *"
  line09 = "* Y for Yes, if you want to stop, type: Q                   *"
  line10 = "* Q to Quit                                                 *"
  

  playerchoice = input(" " + line01 + "\n " + line02 + "\n " + line03 + "\n " + line04 + "\n " + line05 + "\n " + line06 + "\n " + line07 + "\n " + line01 + "\n\n Enter your choice: ")

  player = int(playerchoice)
  if player < 1 or player > 3:
      print("Invalid input. Please try again.")
      sys.exit("You must enter a number:\n\n 1, 2, or 3.")

  computerchoice = random.choice("123")

  computer = int(computerchoice)

  print("")
  print("You chose: " + str(RPS(player)).replace('RPS.', '') + ".")
  print("The computer chose: " + str(RPS(computer)).replace('RPS.', '') + ".")
  print("")

  if player == 1 and computer == 3:
      print("Rock crushes scissors. 🎉 You win!")
  elif player == 2 and computer == 1:
      print("Paper covers rock. 🎉 You win!")
  elif player == 3 and computer == 2:
      print("Scissors cuts paper. 🎉 You win!")
  elif player == computer:
      print("It's a tie. 😐")
  else:
      print(" 😢 You lose. 🎉 Computer wins!")

  playagain = input(" " + line01 + "\n " + line08 + "\n " + line09 + "\n " + line10 + "\n " + line01 + "\n\n Enter your choice: ")

  if playagain.lower() == "y":
      continue
  else:
      print("\n 🎉🎉🎉🎉 \n")  
        
      title = " End Game: Rock, Paper, Scissors (RPS) ".upper()
      print(title.center(50, "" + ("=") + ""))
      print ("Thank you for playing the game of Rock, Paper, Scissors (RPS)!")
      print ("")
      playagain = False

sys.exit("Bye! Bye! Bye! 👋👋👋 \n\n")


   
  

