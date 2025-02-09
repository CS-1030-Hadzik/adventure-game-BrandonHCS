
#Brings an introduction to the player, likely will stay the same
def IntroductoryScript(PlayerName):
    print(f"\nYou find yourself waking up with a pounding headache. A warm orange light glows on the other side of the room as you. \"Are you okay, {PlayerName}?\" You try to respond, but all you can manage in this moment is a slight groan. \"You took a pretty heavy blow to the head and were out for a while. Luckily I found us some cover in this cave, so we should be safe for now.\" Your companion's voice grows closer and clearer as your headache lessens slightly, sounding deep and gravelly. \"We should probably stay here for a few more hours at least.\"\n\nDo you stay?")
    return input("input the # indicated between the '#' to respond\n'1' Stay here with your companion\n'2' Try your luck on the road\n")
#Adds a new choice and consenquences from the previous one in
def SecondDecision(PlayerName, FirstChoice):
    if(FirstChoice == "2"):
        #possibly find a way to allow the player to go back on their decision efficiently, selecing a choice will change their previous choice to a one and run through the first option's dialoge (maybe something like pointers in c++?)
        print(f"You stand, ignoring your companion's recommendation and protests, head pounding, and begin stumbling towards the cave mouth. Getting outside, you realize you don't actually know where you are.\n\n")
        playerchoice = input("'1' Follow the path to the right\n'2' Follow the path to the left\n'3' Blaze your own trail, for you are not a coward!\n")
    elif(FirstChoice == "1"):
        print(f"\"Good, {PlayerName}. Glad you still have some reason about you. I'm sure you must be at least somewhat confused, but I think it's best if we rest for now and I'll answer your questions on the road in the morning.\" Your companion rises from next to you and, from the sounds of it, walks a few paces away before lying down. It's probably best you get some sleep as well.\n\nYou awaken in the morning to the sun's bright rays shining in through the mouth of a cave. While you still don't remember where or who you are, if your companion says it's best to get a move on, it's likely best to get moving.\n\"We've got a long walk east to get to Phalen, so I can likely answer some of your questions now.\"\n\n")
        return input("What do you want to ask?\n'1' What are we doing out here?\n'2' Who are you?")
    else:
        print("Did you forget to follow instructions? Play properly or else this goes nowhere. You died from the head trauma.")