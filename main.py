# Imports
import time
import random
import sys
import os
# Variables

# Functions
def text(toprint, speed):
 geranium = 1
 for i in toprint:
  os.system('clear')
  print(toprint[0:geranium])
  time.sleep(speed)
  geranium = geranium+1
# Begin code
text("Welcome to the world of 1763 Britain! You are King George III, and your country has just won the French and Indian War, garnering your country all of New France and a significant portion of the Americas!", 0.1)
text("However, this victory has increased the national debt to €113M. Your job as king is to pay off the national debt before you die in 57 years and avoid revolutionary war with New England.", 0.1)