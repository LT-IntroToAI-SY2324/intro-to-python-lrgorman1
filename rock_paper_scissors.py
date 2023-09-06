# We will write a rock paper scissors game in class - Complete it in this file
import random

player_choice = "scisors"
computer_choice = "paper"

# Create function that gets choci==ices

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = "rock"
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer":computer_choice}

    return choices
choices = get_choices()
print(choices)