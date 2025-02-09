"""
Author: Brandon
Version: 0.8
Description: This is the adventure game assignment, by the end of the 
project (if I remember correctly) I'll need to have at least three 
different choices with multiple options for each
"""

import gamefuns
#pull the player's name. This will be how the system refers to them for the rest of the game.
PlayerName = input("How would you like me to refer to you, user? \n")
#Welcome them to the game, edit to fit the tone of the game later if needed
print(f"Welcome to the adventure game {PlayerName}!\nYour adventure will begin shortly.")

#runs a function created in the library in gamesfun.py to run the beginning of the script, may need to learn a bit more about python returning for more advanced stats than just tracking each decision
FirstChoice = gamefuns.IntroductoryScript(PlayerName)
SecondChoice = gamefuns.SecondDecision(PlayerName, FirstChoice)